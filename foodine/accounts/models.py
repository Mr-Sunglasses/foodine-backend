from django.db import models


# Create your models here.

class Costumer(models.Model):
    name = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=255, null=True)
    email = models.CharField(max_length=255, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.name} Created at:  {self.date_created}"