# mockdata/management/commands/generate_mock.py
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
import random

class Command(BaseCommand):
    help = "Genera usuarios ficticios y relaciones de ex parejas"

    def handle(self, *args, **kwargs):
        nombres = ["Ana", "Luis", "Carlos", "María", "Lucía", "Pedro", "Laura", "Javier"]
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