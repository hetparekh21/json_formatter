from django.contrib import admin

from json_main.models import UserModel, saved_jsons

# Register your models here.

admin.site.register(UserModel)

admin.site.register(saved_jsons)
