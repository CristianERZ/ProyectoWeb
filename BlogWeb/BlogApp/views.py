from django.shortcuts import render, HttpResponse

def home(request):

    return render(request, 'BlogApp/home.html')
#-----------------------------------
def info(request):

    return render(request, 'BlogApp/info.html')
#-----------------------------------
def blog(request):

    return render(request, 'BlogApp/blog.html')
#-----------------------------------
def contac(request):

    return render(request, 'BlogApp/contac.html')
#-----------------------------------
