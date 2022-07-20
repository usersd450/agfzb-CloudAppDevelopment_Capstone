from django.db import models
from django.utils.timezone import now


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
    Sedan='Sedan'
    SUV='SUV'
    WAGON='WAGON'
    CHOICES = [
        (Sedan, 'Sedan'),
        (SUV,'SUV'),
        (WAGON,'WAGON')]
    CarModel= models.ForeignKey(CarMake, null=True, on_delete=models.CASCADE)
    name = models.CharField(null=False, max_length=30)
    dealer_id=models.IntegerField()
    Type =models.CharField(null=False,max_length=20,choices=CHOICES)
    year=models.DateField(null=True)
    def __str__(self):
        return "Name: " + self.name + "," + \
                "Type: "+ self.Type +"," + \
                "Dealer_id: " + self.dealer_id +"," +\
                    "Year: " +self.year


# <HINT> Create a plain Python class `CarDealer` to hold dealer data


# <HINT> Create a plain Python class `DealerReview` to hold review data
