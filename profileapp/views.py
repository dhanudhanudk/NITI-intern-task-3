from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"index.html")

def profile(request):
    return render(request,"profile.html")

def Skill(request):
    return render(request,"skill.html")

def Project(request):
    return render(request,"project.html")