## ESTRUCTURA DEL PROYECTO

```
ex-advisor/
├── exadvisor/               ← solo configuración del proyecto
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── reviews/                ← app para la lógica de reseñas
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── templates/              ← HTML base (home, login, etc.)
│   ├── home.html
│   └── login.html
├── users/                  ← app para login/registro/logout
│   ├── __init__.py
│   ├── forms.py
│   ├── urls.py
│   └── views.py
├── .gitignore
├── autosave.sh
├── manage.py
├── README.md
└── requirements.txt
```

## Guardado automático del repositorio: 
cd /workspaces/ex-advisor
source venv/bin/activate
./autosave.sh &

## SQLite tips

### abrir el sqlite
sqlite3 db.sqlite3

### revisar las tablas existentes
.tables

### castear cómo aparece la info
.headers on
.mode column
