from django.db import models
from datetime import date

# Create your models here.
class Fruits(models.Model) :
    name= models.CharField(max_length=122)
    price = models.CharField(max_length=122)
    qty = models.CharField(max_length=122)
    date = models.DateField( default=date.today)

    