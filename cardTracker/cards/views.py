from django.shortcuts import render
from django.http import HttpResponse

from .models import Card

# Create your views here.
def home(request, card_name = "Darkslick Shores"):
   cards = Card.objects.all()
   try: 
      sld_card = Card.objects.get(name= card_name)
   except Card.DoesNotExist:
      return render(request, 'exception.html')
   return render(request, 'home.html', {
      'sld_card': sld_card, 'cards': cards,
   })
