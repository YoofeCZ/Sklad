# flask_app.py
import os
import io
import json
import base64
from flask import Flask, render_template, request, redirect, url_for, jsonify
from PIL import Image
from pyzbar.pyzbar import decode

app = Flask(__name__)

# cesta k data souboru
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, 'sklad.json')

def load_data():
    with open(DATA_FILE, encoding='utf-8-sig') as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

@app.route('/', methods=['GET'])
def index():
    sklad_all = load_data()

    # parametry z query stringu
    q = request.args.get('q', '').strip().lower()
    sklad_filter = request.args.get('sklad_filter', '')
    sort = request.args.get('sort', 'code_asc')

    # filtr podle skladu
    items = {
        code: itm for code, itm in sklad_all.items()
        if not sklad_filter or itm.get('sklad') == sklad_filter
    }

    # vyhledávání v kódu nebo názvu
    if q:
        items = {
            code: itm for code, itm in items.items()
            if q in code.lower() or q in itm['nazev'].lower()
        }

    # klíče pro řazení: čísla (začínají digit) přijdou první, pak písmena
    def key_code(kv):
        code = kv[0]
        return (not code[0].isdigit(), code)
    def key_name(kv):
        name = kv[1]['nazev']
        return (not name[0].isdigit(), name)

    if sort == 'name_asc':
        ordered = dict(sorted(items.items(), key=key_name))
    else:
        ordered = dict(sorted(items.items(), key=key_code))

    return render_template(
        'index.html',
        sklad=ordered,
        q=q,
        sklad_filter=sklad_filter,
        sort=sort
    )

@app.route('/inventory', methods=['GET'])
def inventory():
    sklad_all   = load_data()
    sklad_filter = request.args.get('sklad_filter', '')

    # jen položky pro vybraný sklad (nebo všechny)
    items = {
        code: itm for code, itm in sklad_all.items()
        if not sklad_filter or itm.get('sklad') == sklad_filter
    }

    return render_template(
        'inventory.html',
        items=items,
        sklad_filter=sklad_filter
    )

@app.route('/add', methods=['GET', 'POST'])
def add_item():
    sklad = load_data()
    if request.method == 'POST':
        code  = request.form['code'].strip()
        count = int(request.form.get('count', 1))
        if code in sklad:
            sklad[code]['aktualni_pocet'] += count
            save_data(sklad)
            return redirect(url_for('index'))
        return redirect(url_for('add_new_item', code=code))
    return render_template('add.html')

@app.route('/add/new', methods=['GET', 'POST'])
def add_new_item():
    sklad = load_data()
    if request.method == 'POST':
        code   = request.form['code'].strip()
        name   = request.form['nazev']
        desc   = request.form['popis']
        needed = int(request.form['potrebny_pocet'])
        count  = int(request.form.get('count', 1))
        sklad[code] = {
            'nazev': name,
            'popis': desc,
            'potrebny_pocet': needed,
            'aktualni_pocet': count,
            'sklad': request.form.get('location','')
        }
        save_data(sklad)
        return redirect(url_for('index'))
    code = request.args.get('code', '')
    return render_template('new_item.html', code=code)

@app.route('/remove_count/<code>', methods=['POST'])
def remove_count(code):
    sklad = load_data()
    try:
        count = int(request.form.get('count', 1))
    except ValueError:
        count = 0
    if code in sklad:
        sklad[code]['aktualni_pocet'] = max(0, sklad[code]['aktualni_pocet'] - count)
        save_data(sklad)
    return redirect(url_for('index'))

@app.route('/delete/<code>', methods=['POST'])
def delete_item(code):
    sklad = load_data()
    if code in sklad:
        del sklad[code]
        save_data(sklad)
    return redirect(url_for('index'))

@app.route('/scan-frame', methods=['POST'])
def scan_frame():
    """
    Očekává JSON payload: { "image": "data:image/png;base64,..." }
    Vrací JSON { "codes": ["1234567890123", ...] }
    """
    data = request.get_json(force=True)
    img_data = data.get('image','')
    if ',' in img_data:
        img_data = img_data.split(',',1)[1]
    try:
        img_bytes = base64.b64decode(img_data)
        img = Image.open(io.BytesIO(img_bytes))
    except Exception:
        return jsonify({'codes': [], 'error': 'Nelze zpracovat obrázek'}), 400

    results = decode(img)
    codes = [r.data.decode('utf-8') for r in results]
    return jsonify({'codes': codes})

# Na PythonAnywhere app.run() nevoláme, WSGI to spustí za nás
