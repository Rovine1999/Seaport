from django.contrib import messages
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User, Group
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect


# Create your views here.
from home.decorators import unauthenticated_user


@unauthenticated_user
def register(request):
    if request.method == 'POST':

        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        username = request.POST.get('username')
        pnumber = request.POST.get('pnumber')
        password = request.POST.get('password')
        password1 = request.POST.get('password1')

        if password == password1:
            if not User.objects.filter(email=email).exists():
                if User.objects.filter(username=username).exists():
                    messages.error(request,
                                   'The username has been taken! Please try again with another username.')
                    return redirect('register')
                else:
                    try:
                        validate_password(password)
                        user = User.objects.create(email=email, username=username)
                        user.set_password(password)
                        user.first_name = fname
                        user.last_name = lname
                        # user.userprofile.phone_number = pnumber
                        
                        user.save()
                        messages.success(request, 'You have successfully signed up for an instructor account!')

                        return redirect('login')

                    except ValidationError as e:
                        messages.error(request, f'Password error! {e}')
                        return redirect('register')

            else:
                messages.error(request,
                               'The email has been taken! Please try again with another email.')
                return redirect('register')
        else:
            messages.error(request, 'Passwords do not match!! Please recheck your passwords and try to sign up again')
            return redirect('register')

    return render(request, template_name='admin_/account/register.html', context={'page': 'register'})


@unauthenticated_user
def login_(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have successfully logged In!')
            return redirect('home')
        else:
            messages.error(request, 'Login failed! Check your username and password.')
            return render(request, template_name='admin/account/login.html', context={'page': 'login'})
    return render(request, template_name='admin_/account/login.html', context={'page': 'login'})


def logout_(request):
    logout(request)
    return redirect('login')
