from django.db import models

# Create your models here.

class UserModel(models.Model):
    """Model definition for User."""

    # TODO: Define fields here
    user_id = models.AutoField
    user_name = models.CharField(max_length=255)
    user_email = models.EmailField(max_length=254,unique=True)
    user_password = models.CharField(max_length=255)
    

class saved_jsons(models.Model):
    """Model definition for saved_jsons."""

    # TODO: Define fields here

    saved_id = models.AutoField

    user_id = models.ForeignKey("UserModel",db_column='user_id' , on_delete=models.CASCADE)
    saved_json = models.TextField(default=None, null=True)