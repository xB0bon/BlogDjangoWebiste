
from django.shortcuts import render

def homepage(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def page_notexist(request, exception):
    return render(request, '404error.html')
    

