from django.db import models

# Create your models here.


class Hotel(models.Model):

    name=models.CharField(max_length=100)
    wilaya=models.CharField(max_length=100)
    address=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name

