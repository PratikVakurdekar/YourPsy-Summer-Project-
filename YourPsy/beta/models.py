from django.db import models

# Create your models here.
class Users_Info(models.Model):
    user_name= models.CharField(max_length=200)
    user_email= models.CharField(max_length=200)
    user_test= models.CharField(max_length=200)
    user_age= models.CharField(max_length=10)
    user_gender= models.CharField(max_length=10)

    def __str__(self):
        return self.user_name

