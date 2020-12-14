from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.contrib import messages


def signin(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('/upload-song')

    return render(request, 'signin.html')


def logout_view(request):
    logout(request)
    return redirect('/')


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')

        user = User.objects.filter(username=username).first()

        if user:
            messages.warning(request, 'User already exists')
            return render(request, 'signup.html')
        else:
            User.objects.create_user(username=username, password=password, email=email)
            messages.success(request, 'User is created successfully!')

    return render(request, 'signup.html')