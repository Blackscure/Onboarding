from django.db import models

from onboard.utils.choices import BUSINESS_CATEGORIES, LOCATION_COUNTY_CHOICES, LOCATION_SUB_COUNTY_CHOICES, LOCATION_WARD_CHOICES


class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    date_of_birth = models.DateField()
    nationality = models.CharField(max_length=100)

    business_name = models.CharField(max_length=100)
    business_categories = models.CharField(max_length=100, choices=BUSINESS_CATEGORIES) 
    business_registration_date = models.DateField()

    county =  models.CharField(max_length=100, choices=LOCATION_COUNTY_CHOICES)
    sub_county =  models.CharField(max_length=100, choices=LOCATION_SUB_COUNTY_CHOICES)
    ward =  models.CharField(max_length=100, choices=LOCATION_WARD_CHOICES)
    building_name = models.CharField(max_length=100)
    floor = models.CharField(max_length=100)

    def age_of_business(self):
        from datetime import date
        today = date.today()
        return today.year - self.business_registration_date.year

    def __str__(self):
        return self.name







   



