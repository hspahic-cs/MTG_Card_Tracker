from django.shortcuts import render
from django.http import HttpResponse

from .models import Card

# Create your views here.
def home(request):
   cards = Card.objects.all();