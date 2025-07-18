from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

def users_list():
    usuarios = User.objects.all()
    print(usuarios)


