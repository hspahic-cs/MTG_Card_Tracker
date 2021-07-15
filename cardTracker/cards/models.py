from django.db import models

class Card(models.Model):
    name = models.CharField(max_length = 100)
    quantity = models.IntegerField()
    cardSet = models.CharField(max_length = 50)
    cost = models.DecimalField(decimal_places = 2, max_digits = 5)
    img = models.URLField(max_length=200, default="")

    def __str__ (self):
        return self.name
