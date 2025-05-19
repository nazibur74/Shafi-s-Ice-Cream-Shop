from django.contrib import admin
from myapp.models import Contact
from myapp.models import IceCream, MilkShake, FamilyCombo
from myapp.models import Order

# Register your models here.
admin.site.register(Contact)
admin.site.register(IceCream)
admin.site.register(MilkShake)
admin.site.register(FamilyCombo)
admin.site.register(Order)