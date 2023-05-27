from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .models import Slide, MenuItem
from products.models import Product
from .forms import NewUserForm


def main(request):
    slider = Slide.objects.all()
    return render(request, "index.html", {"slider": slider})


def sign_up(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/")
    form = NewUserForm()
    return render(request, "sign-up.html", {"form": form})


def sign_in(request):
    if request.method == "POST":
        user = authenticate(username=request.POST.get("username"), password=request.POST.get("password"))
        if user:
            login(request, user)
            return redirect('/')
    return render(request, "sign-in.html")


def sign_out(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect("/")