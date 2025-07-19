from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

def users_list():
    usuarios = User.objects.all()
    print(usuarios)


def create_user(username=str, password=str):
    # Comrpueba si existe el usuario

    # Crea el usuario+
    User.objects.create_user(username=username, password=password)

    # Avisamos de que se ha creado correctamente
    print(f"Usuario {username} creado correctamente")



