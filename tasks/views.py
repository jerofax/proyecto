from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User

def home(request):
   return render(request, "home.html")

def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            username = user.username
            if len(username) == 10:
                return redirect("/profesor/")
            elif len(username) == 8:
                return redirect("/estudiante/")
        else:
            error_msg="Usuario o contraseña incorrectos"
            return render(request, 'login.html', {'error_msg': error_msg})
    
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def estudiante(request):
    user = request.user
    if len(user.username) == 8:
        return render(request, "estudiante.html", {'nombre': user.first_name})
    else:
        return redirect("/signin/")  # Redirigir si el usuario no tiene el username de 8 dígitos

def profesor(request):
    user = request.user
    if len(user.username) == 10:
        return render(request, "profesor.html", {'nombre': user.first_name})
    else:
        return redirect("/signin/")  # Redirigir si el usuario no tiene el username de 10 dígitos
