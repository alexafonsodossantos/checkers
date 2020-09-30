from django.contrib import admin

# Register your models here.
from .models import model_pizza
admin.site.register(model_pizza)