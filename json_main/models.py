from django.db import models

# Create your models here.

class UserModel(models.Model):
    """Model definition for User."""

    # TODO: Define fields here
    user_id = models.AutoField
    user_name = models.CharField(max_length=255)
    user_email = models.EmailField(max_length=254,unique=True)
    user_password = models.CharField(max_length=255)

    # make to string method
    def __str__(self):
        return self.user_id

    # make tojson method
    def tojson(self):
        return {
            'user_id' : self.user_id,
            'user_name' : self.user_name,
            'user_email' : self.user_email,
            'user_password' : self.user_password
        }

    
            
class saved_jsons(models.Model):
    """Model definition for saved_jsons."""

    # TODO: Define fields here

    saved_id = models.AutoField

    user_id = models.ForeignKey(UserModel , on_delete=models.CASCADE)
    saved_json = models.TextField(default=None, null=True)