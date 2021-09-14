from django.shortcuts import render
from django.db import models
from django.views import View
from .models import Laptop
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView

# Create your views here.
class LaptopListview(ListView):
    model = Laptop
 


class LaptopCreateview(CreateView):
    model = Laptop
  
    fields = '__all__'
    success_url = '/lap/list'

class LaptopUpdateview(UpdateView):
    model = Laptop
 
    fields = '__all__'
    success_url = '/lap/list'

class LaptopDeleteview(DeleteView):
    model = Laptop
  
    success_url = '/lap/list'



