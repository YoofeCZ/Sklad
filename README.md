# 📦 Skladová aplikace (Flask + Čárové kódy)

Moderní webová aplikace pro správu skladu s podporou čárových kódů. Umožňuje efektivní přidávání, odečítání a inventarizaci položek s intuitivním rozhraním a možností použití skeneru nebo webkamery.

![Platform](https://img.shields.io/badge/platform-web-lightgrey)
![Build](https://img.shields.io/badge/build-passing-brightgreen)
![License](https://img.shields.io/github/license/yourusername/yourrepo)
![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![Flask](https://img.shields.io/badge/flask-2.x-orange)

---

## ✨ Funkce

- 📷 **Skenování čárových kódů** pomocí webkamery nebo skeneru
- ➕ **Přidávání položek** podle naskenovaného kódu
- ✏️ **Vytváření nových záznamů**, pokud položka v systému neexistuje
- 🔢 **Odečítání počtů kusů** při spotřebě nebo výdeji
- 🧮 **Inventura skladu** se živou kontrolou chybějících položek
- 🔍 **Vyhledávání, filtrování a řazení** položek podle názvu, kódu nebo skladu
- 📊 **Zobrazení rozdílů** mezi požadovaným a aktuálním stavem

---

## 🧰 Použité technologie

| Kategorie         | Technologie               |
|------------------|---------------------------|
| Backend          | [Python 3.8+](https://www.python.org/), [Flask](https://flask.palletsprojects.com/) |
| Frontend         | HTML5, CSS3, JavaScript (vanilla), SweetAlert2 |
| Databáze         | JSON (`sklad.json`)       |
| Kódové skenování | [pyzbar](https://github.com/NaturalHistoryMuseum/pyzbar), [Pillow](https://pillow.readthedocs.io/) |
| Deployment       | Kompatibilní s WSGI / PythonAnywhere |

---

## 🚀 Instalace

> Vyžaduje Python 3.8+ a `pip`

```bash
git clone https://github.com/yourusername/yourrepo.git
cd yourrepo
pip install -r requirements.txt
```

Pokud neexistuje, vytvoř soubor `sklad.json`:

```json
{}
```

Spusť aplikaci:

```bash
python flask_app.py
```

Aplikace poběží na `http://127.0.0.1:5000`.

---

## 📂 Struktura projektu

```csharp
templates/
  ├── index.html
  ├── add.html
  ├── new_item.html
  ├── remove.html
  └── inventory.html
sklad.json         # Datový soubor
flask_app.py       # Backend server
```

---

## 🖥️ Podporované prohlížeče

| Prohlížeč        | Stav       |
|------------------|------------|
| Chrome           | ✅ Funkční |
| Firefox          | ✅ Funkční |
| Edge             | ✅ Funkční |
| Safari (iOS)     | ✅ Funkční |
| Opera            | ✅ Funkční |

---

## 🔐 Bezpečnost

- Lokální aplikace, není určena pro veřejný provoz bez přístupového systému.
- Pro produkční nasazení doporučujeme přidat autentifikaci (např. Flask-Login).

---

## 🌍 Lokalizace

Aplikace je plně v **češtině** a lze ji jednoduše přeložit do jiného jazyka pomocí Jinja2 šablon.

---

## 🔧 Možnosti rozšíření

- Export do CSV nebo Excelu
- Historie změn
- Uživatelský systém s přihlašováním
- Automatické notifikace při nedostatku zásob

---

## 🤝 Přispěvatelé

- 👨‍💻 **Dominik** – vývojář
- 📚 Ostatní knihovny – pyzbar, Pillow, Flask, SweetAlert2

---

## 📝 Licence

Tento projekt je licencován pod [MIT licencí](LICENSE).

---

## 🧩 Verze

```yaml
Verze: 1.0.0
Datum: Květen 2025
```

---

## 💬 Kontakt

Máš nápady na vylepšení? Klidně vytvoř issue nebo mě kontaktuj.

```nginx
Dominik – vývojář aplikace
```
