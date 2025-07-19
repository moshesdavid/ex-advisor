from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

def users_list():
    usuarios = User.objects.all()
    return usuarios

def check_user_exist(username):
    """
    Función que revisa si existe un usuario y devuelve True/False
    """    
    # Recuperamos el nombre de los usuarios
    usuarios = users_list()

    # Revisamos si el usuario existe en la lista
    if username in usuarios:
        return True
    else:
        return False


def create_user(username=str, password=str):
    # Comrpueba si existe el usuario
    user_exist = check_user_exist(username)

    if user_exist:
        # Crea el usuario
        User.objects.create_user(username=username, password=password)

        # Avisamos de que se ha creado correctamente
        print(f"Usuario {username} creado correctamente")

    else:
        print(f"El usuario {username} ya existe. Prueba con otro nombre.")



