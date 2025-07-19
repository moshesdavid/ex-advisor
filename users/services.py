from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

def users_list(show: bool = False) -> list[str]:
    lista_usuarios = [user.username for user in User.objects.all()]     
    if show==True:
        print(f"Lista usuarios actual: {lista_usuarios}")
    return lista_usuarios

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

def create_user(username=str, password=str, email=str):
    # Comrpueba si existe el usuario
    user_exist = check_user_exist(username)

    if user_exist:
        # Crea el usuario
        User.objects.create_user(username=username, password=password, email=email)

        # Avisamos de que se ha creado correctamente
        print(f"Usuario {username} creado correctamente")

    else:
        print(f"El usuario {username} ya existe. Prueba con otro nombre.")

def user_info(username:str, show:bool = False):
    """
    Devuelve la información de un usuario concreto
    """
    user = User.objects.filter(username=username).first()
    if show:
        print(f"Información del usuario: ")
        print(f"Usuario: {user.username}")
        print(f"Password: {user.password}")    
    return user



