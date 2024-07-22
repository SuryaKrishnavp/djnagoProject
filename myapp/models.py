from django.db import models

# Create your models here.
class Users(models.Model):
    Name=models.CharField(max_length=50)
    Email=models.CharField(max_length=50)
    Phonenumber=models.IntegerField()
    Password=models.CharField(max_length=50)

    def __str__(self):
        return self.Name


class Todo(models.Model):
    owner=models.ForeignKey(Users,related_name="user", on_delete=models.CASCADE)
    Activity=models.CharField(max_length=50)
    Priority=models.CharField(max_length=50)
    Image=models.ImageField(upload_to='static/images')
    Date=models.CharField(max_length=30)
    Time=models.CharField(max_length=10)

    def __str__(self):
        return self.Activity
