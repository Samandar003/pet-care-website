from django.shortcuts import render



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

    return render(request, 'base/login_register.html')

def loginPage(request):

    return render(request, 'base/login_register.html')



    