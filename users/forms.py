from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

def register_user(username, password, email):
    if User.objects.filter(username=)