from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from myapp.models import Contact
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from myapp.models import IceCream, MilkShake, FamilyCombo
from myapp.forms import OrderForm


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

from myapp.models import IceCream, MilkShake, FamilyCombo

def ice_cream(request):
    flavors = IceCream.objects.all()
    return render(request, 'ice_cream.html', {'flavors': flavors})

def ice_cream_detail(request, pk):
    ice_cream = get_object_or_404(IceCream, pk=pk)

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.ice_cream = ice_cream
            order.save()
            messages.success(request, "Your order has been placed successfully!")
            return redirect('ice_cream_detail', pk=pk)
    else:
        form = OrderForm()

    return render(request, 'ice_cream_detail.html', {
        'flavor': ice_cream,
        'form': form
    })

def milk_shake(request):
    milkshakes = MilkShake.objects.all()
    return render(request, 'milk_shake.html', {'milkshakes': milkshakes})

def family_combo(request):
    combos = FamilyCombo.objects.all()
    return render(request, 'family_combo.html', {'combos': combos})
