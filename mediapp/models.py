from django.db import models

# Create your models here.
class patient(models.Model):
    full_name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.full_name

class doctor(models.Model):
    full_name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    email = models.EmailField()
    status = models.CharField(max_length=100)
    age = models.IntegerField()
    qualification = models.CharField(max_length=100)
    def __str__(self):
        return self.full_name

    #create a staff model
    #firstname,lastname,position,phonenumber,email,hire date
    #should return first and last name

    #create a ward
    #name,totalbeds,availablebeds
    #return the name

class staffmember(models.Model):
        first_name = models.CharField(max_length=100)
        last_name = models.CharField(max_length=100)
        position = models.CharField(max_length=100)
        phone_number = models.CharField(max_length=100)
        email = models.EmailField()
        hiredate = models.DateField()

        def __str__(self):
            return self.first_name + " " + self.last_name


class ward(models.Model):
    name = models.CharField(max_length=100)
    totalbeds = models.IntegerField()
    bedsavailable = models.IntegerField()
    def __str__(self):
        return self.name


class Appointment(models.Model):
    name = models.CharField(max_length=100)
    email= models.EmailField()
    phone = models.CharField(max_length=100)
    date = models.DateField()
    department = models.CharField(max_length=100)
    doctor = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name

class contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    def __str__(self):
        return self.name

































