## ESTRUCTURA DEL PROYECTO ##
ex-advisor/
├── manage.py
├── requirements.txt (opcional)
├── exadvisor/           ← solo configuración del proyecto
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── templates/           ← HTML base (home, login, etc.)
│   ├── home.html
│   └── login.html
├── users/               ← app nueva para login/registro/logout
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── ...
├── reviews/             ← app para la lógica de reseñas
│   ├── views.py
│   ├── models.py
│   ├── urls.py
│   └── ...


## Guardado automático del repositorio: 
cd /workspaces/ex-advisor
source venv/bin/activate
./autosave.sh &

