from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from .forms import MyUserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

def home(request):
    
    context = {}
    return render(request, 'base/index.html', context)

def blog(request):
    return render(request, 'base/blog.html')

def about(request):
    return render(request, 'base/about.html')

def booking(request):
    return render(request, 'base/booking.html')

def contact(request):
    return render(request, 'base/contact.html')

def price(request):
    return render(request, 'base/price.html')

def service(request):
    return render(request, 'base/service.html')

def single(request):
    return render(request, 'base/single.html')

def registerPage(request):
    page = 'register'
    form = MyUserCreationForm()
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Something went wrong!!!')

    context = {'form':form, 'page':page}
    return render(request, 'base/login_register.html', context)

def loginPage(request):
    page = 'login'
    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']
        try:

            user = User.objects.filter(username=username).first()
        except:
            messages.error(request, 'User Not Found!!!')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username Or password is incorrect')
    context = {'page':page, 'messages':messages}
    return render(request, 'base/login_register.html', context)


def createBooking(request):
    if request.method == 'POST':
        name = request.POST['name'].lower()
        email = request.POST['email']
        reservation_date = request.POST['reservation_date']
        reservation_time = request.POST['reservation_time']
        service = request.POST['service']
        try:
            booking = Booking.objects.create(
                name=name,
                email=email,
                reservation_date=reservation_date,
                reservation_time=reservation_time,
                service=service
            )
            booking.save()
            return HttpResponse('You are booked')
        except:
            return HttpResponse('You are already booked')

def createnewsletter(request):
    if request.method == 'POST':
        name = request.POST['name'].lower()
        email = request.POST['email']
        try:
            newsletter = Newsletter.objects.create(
                name = name,
                email = email
            )
            newsletter.save()
            return HttpResponse('You are enrolled for newsletter')    
        except:
            return HttpResponse('You are already enrolled for newsletter')    


