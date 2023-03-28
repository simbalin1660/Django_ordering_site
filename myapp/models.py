from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)

class NewTable(models.Model):
    bigint_f = models.BigIntegerField()
    bool_f = models.BooleanField()
    date_f = models.DateField(auto_now=True)
    char_f = models.CharField(max_length=20, unique=True)
    datetime_f = models.DateTimeField(auto_now_add=True)
    decimal_f = models.DecimalField(max_digits=10, decimal_places=2)
    float_f = models.FloatField(null=True)
    int_f = models.IntegerField(default=2010)
    text_f = models.TextField()

class Product(models.Model):
    type = (('110', 'SN1-110'),
            ('160', 'SN1-160'),
            ('200', 'SN1-200'),
            )
    W_L = (('1', '1160x1680'),
           ('2', '1300x1985'),
           ('3', '1480x2113'),
           )
    CWH = (('1', '350'),
           ('2', '400'),
           ('3', '450'),
           )
    mail = models.EmailField(max_length=200)
    Type = models.CharField(max_length=10, choices=type)
    WidthAndLength = models.CharField(max_length=10, choices=W_L)
    ClosedWorkingHeight = models.CharField(max_length=10, choices=CWH)

    def __unicode__(self):
        return self.Type

class Expense(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
