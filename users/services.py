from django.conf import settings
from django.core.exceptions import ValidationError
from datetime import date
from users.models import Pareja
from django.contrib.auth import get_user_model

User = get_user_model()

def users_list(show: bool = False) -> list[str]:
    lista_usuarios = [user.username for user in User.objects.all()]
    if show:
        print(f"Lista usuarios actual: {lista_usuarios}")
    return lista_usuarios


def check_user_exist(username):
    """
    Función que revisa si existe un usuario y devuelve True/False
    """
    usuarios = users_list()
    return username in usuarios


def create_user(
    username: str,
    first_name: str,
    last_name: str,
    date_of_birth: date,
    password: str,
    email: str,
    es_fake: bool = False
):
    user_exist = check_user_exist(username)

    if not user_exist:
        User.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            date_of_birth=date_of_birth,
            password=password,
            email=email,
            es_fake=es_fake
        )
        print(f"Usuario {username} creado correctamente")
    else:
        print(f"El usuario {username} ya existe. Prueba con otro nombre.")


def user_info(username: str, show: bool = False):
    """
    Devuelve la información de un usuario concreto
    """
    user = User.objects.filter(username=username).first()
    if show and user:
        print("Información del usuario:")
        print(f"Usuario: {user.username}")
        print(f"Password: {user.password}")
    return user

def crear_pareja(
    username1: str,  
    username2: str,
    solicitante: str,
    fecha_inicio: date = date.today(),
    fecha_fin: date = None
):
    # Revisar que los usuarios existen
    if not check_user_exist(username1):
        print(f"El usuario {username1} no existe")
        return
    if not check_user_exist(username2):
        print(f"El usuario {username2} no existe")
        return

    # Verificar que el solicitante es uno de los 2 usuarios a relacionar
    if solicitante not in [username1, username2]:
        print(f"El solicitante debe ser uno de los dos usuarios a relacionar")
        return
    
    # Revisar que no se ha registrado ya una relación entre los usuarios para esas fechas
    # TODO: pendiente de contar con la tabla de parejas para poder comprobar esto

    # Generamos el objeto pareja
    Pareja.objects.create(
        miembro_1=User.objects.get(username=username1),
        miembro_2=User.objects.get(username=username2),
        fecha_inicio=fecha_inicio,
        fecha_fin=fecha_fin,
        solicitante=User.objects.get(username=solicitante)
    )
    
    print(f"Pareja creada con éxito entre {username1} y {username2} desde {fecha_inicio} hasta {fecha_fin} solicitado por {solicitante}")




