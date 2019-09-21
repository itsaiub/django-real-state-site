from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
# Create your views here.


def register(request):
    if request.method == 'POST':
        # Register User
        # get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # check passwor match
        if password == password2:
            # check username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'That username is taken')
                return redirect('accounts:register')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'That email is taken')
                return redirect('accounts:register')
            else:
                user = User.objects.create(
                    username=username,
                    first_name=first_name,
                    last_name=last_name,
                    email=email
                )
                user.set_password(password)
                # auth.login(request, user)
                # messages.success(request, 'register successful')
                # return redirect('pages:index')
                user.save()
                messages.success(
                    request, 'You are now registered and can log in')
                return redirect('accounts:login')
        else:
            messages.error(request, 'Password do not match')
            return redirect('accounts:register')
    return render(request, 'accounts/register.html')


def login(request):
    if request.method == 'POST':
        # Login User
        pass
    return render(request, 'accounts/login.html')


def logout(request):
    return redirect('pages:index')


def dashboard(request):

    return render(request, 'accounts/dashboard.html')
