# 🛠️ ll-db-builder

**ll-db-builder** is a professional Python project that automatically sets up the PostgreSQL database for Flask-based or general systems using SQLAlchemy.  
It loads connection settings from `.env`, ensures the database exists, and creates all required tables based on the defined models in `main/models`.

---

## 🚀 Features

- ✅ Initializes all tables using SQLAlchemy
- ✅ Secure loading of settings via `.env`
- ✅ Clean and professional project structure
- ✅ Ready to integrate with CI or Flask projects

---

## 📁 Project Structure

```bash
ll-db-builder/
├── main/
│   ├── config/         # Environment and configuration loading
│   ├── models/         # Database models
│   └── extensions.py   # SQLAlchemy configuration
├── .env                # Database connection settings
├── build.py            # Main script to initialize DB and tables
├── requirements.txt    # Main project dependencies
├── test-requirements.txt  # Test-specific dependencies
└── README.md           # This file
```

---

## ⚙️ Usage

### 1. Create a virtual environment

```bash
python -m venv venv
venv\Scripts\activate  # On Windows
# or
source venv/bin/activate  # On Linux/Mac

pip install -r requirements.txt
```

### 2. Configure environment variables

Create a `.env` file in the root directory with:

```env
DB_NAME=ll_db
DB_USER=postgres
DB_PASSWORD=yourpassword
DB_HOST=127.0.0.1
DB_PORT=5432
```

### 3. Run the script

```bash
python build.py
```

---

## 🧱 Key Files

| File | Purpose |
|------|---------|
| `build.py` | Entry point – loads config and builds database/tables |
| `config_loader.py` | Loads environment variables |
| `db_initializer.py` | Ensures DB exists and initializes tables |
| `models/*.py` | SQLAlchemy table definitions |
| `extensions.py` | Defines `db` and `Base` for reuse |

---

## 🧪 Testing (Optional)

```bash
pip install -r test-requirements.txt
pytest
```

---

## 📝 License

MIT License – See [LICENSE](LICENSE) for details.

---

## 👨‍💻 Author

- **Tamer Faour** – [@TamerOnLine](https://github.com/TamerOnLine)