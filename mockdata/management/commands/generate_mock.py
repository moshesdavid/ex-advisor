# mockdata/management/commands/generate_mock.py
from django.core.management.base import BaseCommand
from django.conf import settings
import random
from faker import Faker
from users.services import create_user
import unicodedata

def normalizar_contacto(contacto: str):
    """
    This function normalizes a contact string by removing spaces and accents.   
    """
    contacto_sin_espacios = contacto.replace(" ", "")
    contacto_sin_tildes = unicodedata.normalize('NFKD', contacto_sin_espacios).encode('ascii', 'ignore').decode('utf-8')
    return contacto_sin_tildes

def create_fake_users(n_users: int):
    """
    This function creates a specified number of users with random names and emails.
    It uses the Faker library to generate realistic names and emails.
    It also normalizes the names to create valid usernames and emails.
    It prints the created users' names and emails.
    """
    if n_users <= 0:
        print("Número de usuarios no válido.")
        return
    else:
        print(f"Creando {n_users} usuarios...")
        # Inicializar Faker con el locale español
        # Esto asegura que los nombres y apellidos generados sean en español
        faker = Faker('es_ES')

        # Crear usuarios
        for _ in range(n_users):
            # Generar datos base de usuario
            
            first_name = faker.first_name()
            last_name = faker.last_name()
            date_of_birth = faker.date_of_birth(minimum_age=18, maximum_age=65)
            es_fake = True

            # Normalizar el nombre y apellido para crear campos adicionales
            norm_first_name = normalizar_contacto(first_name).lower()
            norm_last_name = normalizar_contacto(last_name).lower()
        
            # Creamos campos adicionales
            username = f"{norm_first_name}.{norm_last_name}"
            email = f"{norm_first_name}.{norm_last_name}@gmail.com"

            # Llamar a la función create_user para crear el usuario
            print(f"Creando usuario: {username}")
            print(f"Con email: {email}")
            print(f"Con fecha de nacimiento: {date_of_birth}")
            print(f"Es fake: {es_fake}")
            print(f"Con password: test1234")

            create_user(
                username=username,
                first_name=first_name,
                last_name=last_name,
                date_of_birth=date_of_birth,
                password="test1234",
                email=email,
                es_fake=es_fake
            )
            print(f"Usuario creado: {username} con email: {email}")

# Creamos la clase para django
class Command(BaseCommand):
    help = "Genera usuarios ficticios y relaciones de ex parejas"

    def add_arguments(self, parser):
        parser.add_argument('--n_users', type=int, default=1, help='Número de usuarios a generar')

    def handle(self, *args, **options):
        n = options['n_users']
        create_fake_users(n)
        self.stdout.write(self.style.SUCCESS(f"{n} usuario(s) ficticio(s) creados correctamente."))

"""
class Command(BaseCommand):
    help = "Genera usuarios ficticios y relaciones de ex parejas"

    def handle(self, *args, **kwargs):        nombres = ["Ana", "Luis", "Carlos", "María", "Lucía", "Pedro", "Laura", "Javier"]
        apellidos = ["Gómez", "Pérez", "López", "Martínez", "Sánchez", "Fernández", "Ruiz", "Torres"]

        # Crear 10 usuarios
        for i in range(10):
            nombre = random.choice(nombres)
            apellido = random.choice(apellidos)
            username = f"{nombre.lower()}{apellido.lower()}{i}"
            email = f"{username}@example.com"
            password = "test1234"
            
            if not User.objects.filter(username=username).exists():
                User.objects.create_user(username=username, email=email, password=password)
                self.stdout.write(self.style.SUCCESS(f"Usuario creado: {username}"))

        # Aquí podrías crear relaciones si tienes un modelo de "relación de ex-parejas"
"""


