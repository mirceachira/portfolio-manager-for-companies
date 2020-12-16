from django.db import models

class Company(models.Model):
    "Default Company Model for Portfolio Manager for Companies"

    # Each company has a name, description, contact email/phone, and adress
    name=models.TextField(null=False,blank=False,help_text="company's name")
    description=models.TextField(null=False,blank=False,help_text="description of the company")
    email=models.TextField(null=False,blank=False,help_text="company's email")
    phone=models.TextField(null=False,blank=False,help_text="company's phone")
    adress=models.TextField(null=False,blank=False,help_text="company's adress")

    # Optionally, the companies can add their size and what technologies are using
    #size=models.TextField(null=True,blank=True,help_text="company's size")
    #technologies=models.TextField(null=True,blank=True,help_text="company's technologies")

