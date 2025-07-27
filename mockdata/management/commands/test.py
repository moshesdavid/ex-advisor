from faker import Faker
import unicodedata

def normalizar_contacto(contacto: str):
    """
    Recibe un string y lo castea para quitar espacios y/o tildes.
    """
    contacto_sin_espacios = contacto.replace(" ", "")
    contacto_sin_tildes = unicodedata.normalize('NFKD', contacto_sin_espacios).encode('ascii', 'ignore').decode('utf-8')
    return contacto_sin_tildes

def create_n_users(n_users: int):
    """
    Función que recibe un número de usuarios y los crea con parámetros:
    nombre, apellido, email.
    """
    faker = Faker('es_ES')

    for _ in range(n_users):
        nombre = faker.first_name()
        apellido = faker.last_name()

        nombre_normalizado = normalizar_contacto(nombre).lower()
        apellido_normalizado = normalizar_contacto(apellido).lower()

        email = f"{nombre_normalizado}.{apellido_normalizado}@gmail.com"

        print(f"Nuevo usuario: {nombre} {apellido} con email: {email}")

# Ejecución de prueba
create_n_users(5)

