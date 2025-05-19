from django.db import models

#makemigrations ---> Create changes and store in a file
#migrate ---> Apply the changes created by makemigrations

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class IceCream(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    image_url = models.URLField()

    def __str__(self):
        return self.name

class MilkShake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    image_url = models.URLField()

    def __str__(self):
        return self.name

class FamilyCombo(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    image_url = models.URLField()

    def __str__(self):
        return self.name
    
class Order(models.Model):
    ice_cream = models.ForeignKey(IceCream, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} - {self.ice_cream.name} by {self.name}"