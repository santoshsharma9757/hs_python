from django.db import models
from uuid import uuid4

# Create your models here.
class Cities(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4, editable=False)
    name = models.CharField(max_length=200)
    thumbnail= models.ImageField(upload_to="thumbnail",blank=True, null= True)

    def __str__(self):
        return self.name
    
class Tourism(models.Model):
    city = models.ForeignKey(Cities,on_delete=models.CASCADE,related_name="tourism")
    id = models.UUIDField(primary_key=True,default=uuid4, editable=False)
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="tourism_image")
    about = models.TextField()
    history = models.TextField(blank=True,null=True) # IF Exist
    location = models.TextField()

    def __str__(self):
        return self.name

class TripPlanner(models.Model):
    tourism = models.ForeignKey(Tourism,on_delete=models.CASCADE,related_name='trip_planner')
    id = models.UUIDField(primary_key=True,default=uuid4, editable=False)
    name = models.CharField(max_length=200)
    banner = models.ImageField(upload_to="banner",blank=True,null=True)
    contact_person_name = models.CharField(max_length=200)
    mobile = models.CharField(max_length=15)

    def __str__(self):
        return self.name



class CultureAndTradition(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4, editable=False)
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="culture_tradition_image/",blank=True,null=True)
    about = models.TextField()
    history = models.TextField(blank=True,null=True) # IF Exist

    def __str__(self):
        return self.name

class Food(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4, editable=False)
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="food_image/",blank=True,null=True)
    about = models.TextField(null=True)
    history = models.TextField(blank=True,null=True) # IF Exist

    def __str__(self):
        return self.name

