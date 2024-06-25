from django.db import models
from datetime import datetime
# Create your models here.

class Customer(models.Model):
    full_name=models.CharField(max_length=155,null=True,blank=True)
    email=models.EmailField(unique=True,null=True,blank=True)
    phone_number=models.CharField(max_length=13,null=True,blank=True)
    address=models.CharField(max_length=150,null=True,blank=True)
    joined=models.DateTimeField(default=datetime.now())
    image=models.ImageField(upload_to='customers/customer_imag',null=True,blank=True)


    def __str__(self):
        return self.email

    class Meta:
        ordering=['joined']
        verbose_name_plural = 'Xaridorlar'