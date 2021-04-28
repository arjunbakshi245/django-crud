from django.db import models
import datetime
# Create your models here.


class Healthcare(models.Model):
    name = models.CharField(max_length=30)
    address = models.TextField(max_length=1000)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    group = models.CharField(max_length=20)
    Dentist = models.BooleanField(default=False)
    Opthalmologist = models.BooleanField(default=False)
    Orthopaedic = models.BooleanField(default=False)
    dob = models.DateField(default=datetime.date.today)
    total = models.BooleanField()
    pic = models.ImageField(null=True, blank=True, upload_to="images/")
    amount = models.FloatField()
    # something_truthy = models.BooleanField(required=False)

    class Meta:
        db_table = 'health'
