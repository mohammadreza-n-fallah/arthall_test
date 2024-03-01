from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255,default=None)


    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255) 
    price = models.FloatField()
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='products/', blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,default=None)
    

    def __str__(self):
        return self.name
    

class Factor(models.Model):
    user=models.CharField(max_length=255,default=None)
    product=models.CharField(max_length=255,default=None)
  
    def __str__(self):
        return self.user