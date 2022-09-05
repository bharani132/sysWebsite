from django.db import models
class employee(models.Model):
    e_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    age = models.CharField(max_length=3)
    service = models.CharField(max_length=3)
    details = models.CharField(max_length=40)
    photo = models.ImageField()
class services(models.Model):
    s_id = models.IntegerField(primary_key=True)
    s_name = models.CharField(max_length=10)
    s_content= models.TextField(max_length=80)
    s_photo = models.ImageField()
class customer(models.Model):
    c_id = models.IntegerField(primary_key=True)
    c_name = models.CharField(max_length=10)
    c_content= models.TextField(max_length=80)
    c_photo = models.ImageField()
class project(models.Model):
    p_id = models.IntegerField(primary_key=True)
    p_name = models.CharField(max_length=10)
    p_content= models.TextField(max_length=80)
    p_photo = models.ImageField()
class year_of_service(models.Model):
    y_id = models.IntegerField(primary_key=True)
    y_name = models.CharField(max_length=10)
    y_content= models.TextField(max_length=80)
    y_photo = models.ImageField()



