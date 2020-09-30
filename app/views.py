from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, TemplateView
# Create your views here.
from .models import model_pizza


class HomePageView(TemplateView):
    template_name = "index.html"

class ListaPizzas(ListView):
	model = model_pizza
	context_object_name = 'pizza'