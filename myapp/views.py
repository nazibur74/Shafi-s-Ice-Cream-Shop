from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from myapp.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    # context = {
    #     'variable_name': 'Django'
    # }
    return render(request, 'index.html')
    #return HttpResponse("This is home page")

def about(request):
    return render(request, 'about.html')
    #return HttpResponse("This is about page")

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        contact = Contact(name=name, email=email, phone=phone, message=message, date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent successfully!')
        
    return render(request, 'contact.html')
    #return HttpResponse("This is contact page")

def service(request):
    return render(request, 'service.html')
    #return HttpResponse("This is service page")