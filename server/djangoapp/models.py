from django.db import models
from django.utils.timezone import now
from django.core import serializers 
import uuid
import json


# Create your models here.

# <HINT> Create a Car Make model `
class CarMake(models.Model):
    name = models.CharField(null=False, max_length=30)
    description=models.CharField(null=False, max_length=200)
    def __str__(self):
      return "Name: " + self.name + "," + \
                 "Description: " + self.description


# <HINT> Create a Car Model model `
class CarModel(models.Model):
    id = models.IntegerField(default=1,primary_key=True)
    Sedan='Sedan'
    SUV='SUV'
    WAGON='WAGON'
    CHOICES = [
        (Sedan, 'Sedan'),
        (SUV,'SUV'),
        (WAGON,'WAGON')]
    make = models.ForeignKey(CarMake, null=False, on_delete=models.CASCADE)  
    name = models.CharField(null=False, max_length=30)
    dealer_id=models.IntegerField()
    Type =models.CharField(null=False,max_length=20,choices=CHOICES)
    year=models.DateField(null=True)
    def __str__(self):
        return "Name: " + self.name + "," + \
                "Type: "+ self.Type +"," + \
                "Dealer_id: " + self.dealer_id +"," +\
                    "Year: " +self.year


class CarDealer():
    def __init__(self, address, city, full_name, id, lat, long, short_name, st, zip):
        # Dealer address
        self.address = address
        # Dealer city
        self.city = city
        # Dealer Full Name
        self.full_name = full_name
        # Dealer id
        self.id = id
        # Location lat
        self.lat = lat
        # Location long
        self.long = long
        # Dealer short name
        self.short_name = short_name
        # Dealer state
        self.st = st
        # Dealer zip
        self.zip = zip

    def __str__(self):
        return "Dealer name: " + self.full_name

class DealerReview():
    def __init__(self,dealership,full_name,purchase,review,purchase_date,car_make,car_model,car_year,sentiment,id):
       self.dealership= dealership
       self.full_name= full_name
       self.purchase=purchase
       self.review=review
       self.purchase_date=purchase_date
       self.car_make=car_make
       self.car_model=car_model
       self.car_year=car_year
       self.sentiment=sentiment
       self.id=id

    def __str__(self):
        return "Dealer Review: " + self.review

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                            sort_keys=True, indent=4)


class ReviewPost:

    def __init__(self, dealership, name, purchase, review):
        self.dealership = dealership
        self.name = name
        self.purchase = purchase
        self.review = review
        self.purchase_date = ""
        self.car_make = ""
        self.car_model = ""
        self.car_year = ""

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                            sort_keys=True, indent=4)
