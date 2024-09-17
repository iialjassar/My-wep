from django.shortcuts import render

def index(request):
    return render(request, 'index.html')




def home(request):
    return render(request,"home.html")


def vision(request):
    return render(request,"vision.html")

def Links(request):
    return render(request,"Links.html")

def comint(request):
    return render(request,"comint.html")

