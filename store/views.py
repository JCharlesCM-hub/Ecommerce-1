from django.shortcuts import render, redirect
from .models import Product, Category
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm, UpdateUserForm
from django import forms

def update_user(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        user_form = UpdateUserForm(request.POST or None, instance=current_user)

        if user_form.is_valid():
            user_form.save()
            login(request, current_user)
            messages.success(request, "Usuário foi alterado!!")
            return redirect('home')
        
        return render(request, 'update_user.html', {user_form:user_form})
    else:
        messages.success(request, "Você pricisa está Logado para Acessar!!")
        return redirect('home')

  

def category_summary(request):
    categories = Category.objects.all()
    return render(request, 'category_summary.html', {"categories":categories})

def category(request, foo):
    # Tira traço e insere espaço
    foo = foo.replace('-', ' ')
    try: 
        # Look Up The Category
        category = Category.objects.get(name=foo)
        products = Product.objects.filter(category=category)
        return render(request, 'category.html', {'products':products, 'category':category})
    except:
        messages.success(request, ("Opa! Essa Categoria não existe."))
        return redirect('home')

def product(request,pk):
    product = Product.objects.get(id=pk)
    return render(request, 'product.html', {'product':product})

def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products':products})

def about(request):
    return render(request, 'about.html', {})

def testes(request):
    return render(request, 'testes.html', {})

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,("Você está conectado!"))
            return redirect('home')
        else:
            messages.success(request,("Houve um erro, tente novamente..."))
            return redirect('login')           
    else:
        return render(request, 'login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ('You have been logged out... Thanks for stopping by...'))
    return redirect('home')

def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            # log in user
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Você se registrou com sucesso!!! Seja bem-vindo."))
            return redirect("home")
        else:
            messages.success(request, ("Opa! Houve um problema ao registrar, tente novamente."))
            return redirect('register')
    else:
        return render(request, 'register.html', {'form':form})



