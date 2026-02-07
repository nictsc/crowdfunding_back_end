from django.db import models #plucking out models from the django 
from django.contrib.auth import get_user_model 


# Create your models / database tables here.
class Fundraiser(models.Model): # inheriting the Django Model from models and capturing in the Fundraiser class
    title = models.CharField(max_length=200) # creating a class attribute named title and this becomes a column in the database table
    description = models.TextField()
    goal = models.IntegerField()
    image = models.URLField()
    is_open = models.BooleanField()
    is_deleted = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        get_user_model(), # This will find the user model in settings; so that we use it a single time.
        on_delete=models.CASCADE, #when an owner is deleted, the fundraisers created by this owner will be created.
        related_name='owned_fundraisers'
    )
1
class Pledge(models.Model):
    amount = models.IntegerField()
    comment = models.CharField(max_length=200)
    anonymous = models.BooleanField()
    is_deleted = models.BooleanField(default=False)
    fundraiser = models.ForeignKey(
        'Fundraiser', ## table to be linked 
        on_delete=models.CASCADE, ## delete the fundraiser means to also delete the related pledges
        related_name='pledges' 
    )
    supporter = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='pledges'
    )
