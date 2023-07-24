from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import authenticate, login , logout 
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.urls import reverse

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Perform authentication logic
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page or any other desired page
            return HttpResponseRedirect(reverse('home'))
        else:
            # Authentication failed, handle error
            error_message = "Invalid username or password."  # Customize error message as needed
            return render(request, 'login.html', {'error_message': error_message})

    return render(request, 'login.html')

def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        # Perform signup logic
        if password1 != password2:
            error_message = "Passwords do not match."  # Customize error message as needed
            return render(request, 'signup.html', {'error_message': error_message})
        
        # Check if username is already taken
        if User.objects.filter(username=username).exists():
            error_message = "Username is already taken."  # Customize error message as needed
            return render(request, 'signup.html', {'error_message': error_message})

        # Create new user
        user = User.objects.create_user(username=username, password=password1)
        login(request, user)
        # Redirect to a success page or any other desired page
        return HttpResponseRedirect(reverse('home'))

    return render(request, 'signup.html')


@login_required
def logout_view(request):
    logout(request)
    # Redirect to the desired page after logout
    return HttpResponseRedirect(reverse('login'))
