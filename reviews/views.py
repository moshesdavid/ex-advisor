# reviews/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

@login_required
def home(request):
    return render(request, "home.html", {"usuario": request.user})

def logout_view(request):
    logout(request)
    return redirect("login")