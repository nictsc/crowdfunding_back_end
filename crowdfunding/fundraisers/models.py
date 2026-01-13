from django.db import models #plucking out models from the django 


# Create your models / database tables here.
class Fundraiser(models.Model): # inheriting the Django Model from models and capturing in the Fundraiser class
    title = models.CharField(max_length=200) # creating a class attribute named title and this becomes a column in the database table
    description = models.TextField()
    goal = models.IntegerField()
    image = models.URLField()
    is_open = models.BooleanField()
    date_created = models.DateTimeField(auto_now_add=True)