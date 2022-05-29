from django.db import models

class Students(models.Model):
    GENDER_OPTIONS = [
        ("MALE", 'Male'),
        ("FEMALE", 'Female'),
        ("OTHER", 'Other'),
    ]

    PATH_OPTIONS = [
        ("FS", "Fullstack"),
        ("DS",  "DataScience"),
        ("CE", "CloudEngineer"),
    ]

    fullname = models.CharField(max_length=30)
    mobil = models.IntegerField(null=True)
    email = models.EmailField(max_length=254)
    gender = models.CharField(max_length=10, choices= GENDER_OPTIONS, default="MALE")
    number = models.IntegerField(blank=True, null=True)
    path = models.CharField( max_length=10, choices= PATH_OPTIONS )

    def __str__(self):
        return f"{self.fullname} {self.number}"
