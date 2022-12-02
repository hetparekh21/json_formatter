from django.db import models

# Create your models here.

class UserModel(models.Model):
    """Model definition for User."""

    # TODO: Define fields here
    user_id = models.AutoField
    user_name = models.CharField(max_length=255)
    user_email = models.EmailField(max_length=254,unique=True)
    user_password = models.CharField(max_length=255)

    # def __init__(self,name,email,password):
    #     self.user_name = name
    #     self.user_email = email
    #     self.user_password = password
        
    
# class saved_jsons(models.Model):
#     """Model definition for saved_jsons."""

#     # TODO: Define fields here
#     user_id = models.ForeignKey(UserModel , on_delete=models.CASCADE)
#     saved_json1 = models.CharField()
#     saved_json2 = models.CharField()
#     saved_json3 = models.CharField()
#     saved_json4 = models.CharField()
#     saved_json5 = models.CharField()

    