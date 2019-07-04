from django.db import models

class Person(models.Model):
    first_name  = models.CharField(max_length=50)
    last_name   = models.CharField(max_length=50)

class Phone(models.Model):
    person      = models.ForeignKey(Person, editable=False, on_delete=models.CASCADE)
    phone       = models.CharField(max_length=50, null=True, blank=True)

class Email(models.Model):
    person      = models.ForeignKey(Person, editable=False, on_delete=models.CASCADE)
    email       = models.EmailField(null=True, blank=True)
