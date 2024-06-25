from django.contrib import admin
from django.contrib.auth.models import User

from app.models import Product, Image,Atribute,AtributeValue,ProductAtribute

# Register your models here.

admin.site.register(Product)
admin.site.register(Image)
admin.site.register(Atribute)
admin.site.register(AtributeValue)
admin.site.register(ProductAtribute)