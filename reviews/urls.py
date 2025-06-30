
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "reviews/registration_success.html")
    else:
        form = UserCreationForm()
    return render(request, "reviews/signup.html", {"form":form})




