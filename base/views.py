from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def gallery(request):
    return render(request, 'gallery.html') 

def contact(request):
    return render(request, 'contact.html')   

def news(request):
    return render(request, 'news.html')

def services(request):
    return render(request, 'services.html')