from django.shortcuts import render
from django.http import HttpResponse
from SHSWeb.forms import studentform
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

def account_list(request):
    obj = Students.objects.all()
    return render(request, "account_list.html", {"Stud_list" : obj})