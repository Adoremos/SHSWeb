from django.shortcuts import render
from django.http import HttpResponse
from SHSWeb.forms import studentform, loginform
from SHSWeb.models import Students
# Create your views here.
def contact(request):
    
    return render(request, "contact.html", {})
    
def about(request):

    return render(request, "about.html", {})

def index(request):

    return render(request, "index.html", {})

def register(request):
    if request.POST: 
        obj = Students()
        obj.name = request.POST.get("name", '')
        obj.email = request.POST.get("email", '')
        obj.password = request.POST.get("password", '')
        obj.save()
    form=studentform()
    return render(request, "register.html",{"form" : form})

def login(request):
    if request.POST:
        obj= Students.objects.all()
        namesearch= request.POST.get("name", '')
        for student in obj:
            print(str(namesearch) + "==" + str(student))
            if(str(namesearch) == str(student)):
                return render(request, "success.html", {})
        return render(request, "failed.html", {})
    form = loginform()
    

    return render(request, "login.html", {"form" : form})
    