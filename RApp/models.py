from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Create your models here.
class User(AbstractUser):
    g = [
        ('0','--- Select Your Gender ---'),
        ('1','Male'),
        ('2','Female'),
    ]
    c=[
        ('0','Guest'),
        ('1','Buyer'),
        ('2','Seller'),
        ('3','Deny')
    ]
    mble = models.CharField(max_length=10,null=True,blank=True)
    gdr = models.CharField(choices=g,default='0',max_length=5)
    role_type_appl=models.CharField(choices=c,default='0',max_length=5)
    role_type=models.CharField(choices=c,default='0',max_length=5)
    eid=models.CharField(max_length=10)
    pfimg=models.ImageField(upload_to='Profiles/',default='pfle.png') 

class seProfile(models.Model):
    t = [
        ('0','--- Select your Preference ---'),
        ('1','Residential'),
        ('2','Commercial'),
        ('3','Agriculturial'),
        ('4','Industrial'),
    ]
    sellang=models.CharField(max_length=20)
    selage=models.IntegerField()
    seloc=models.CharField(max_length=50)
    selltypes=models.CharField(choices=t,default='0',max_length=5)
    sellinfo=models.CharField(max_length=200)
    sellexpr=models.IntegerField()
    sellcerti = models.FileField(upload_to='Attachments/')
    sstatus=models.BooleanField(default=False)
    sc=models.OneToOneField(User,on_delete=models.CASCADE)
class byProfile(models.Model):
    m = [
        ('0','--- Select your Preference ---'),
        ('1','Residential'),
        ('2','Commercial'),
        ('3','Agriculturial'),
        ('4','Industrial'),
    ]
    buylang=models.CharField(max_length=20)
    buyage=models.IntegerField()
    buyloc=models.CharField(max_length=50)
    buytypes=models.CharField(choices=m,default='0',max_length=5)
    buyinfo=models.CharField(max_length=200)
    bstatus=models.BooleanField(default=False)
    bc=models.OneToOneField(User,on_delete=models.CASCADE)

class Property(models.Model):
    y = [
        ('s','Select your Property Type'),
        ('1','Residential'),
        ('2','Commercial'),
        ('3','Agricultural'),
        ('4','Industrial'),
    ]
    d = [
        ('a','Available'),
        ('g','Sold'), 
    ]
    proptitle = models.CharField(max_length=200)
    proptype = models.CharField(choices=y,default='s',max_length=15)
    propcity = models.CharField(max_length=200)
    propstate = models.CharField(max_length=200)
    propzipcode = models.CharField(max_length=20)
    propdesc = models.TextField()
    propsqft = models.PositiveIntegerField()
    propprice = models.DecimalField(max_digits=10,decimal_places=2)
    main_photo =models.ImageField(upload_to='Prroperties/',default='prop.png')
    photo_1 = models.ImageField(upload_to='properties/', blank=True, null=True)
    photo_2 = models.ImageField(upload_to='properties/', blank=True, null=True)
    list_date = models.DateTimeField(auto_now_add=True)
    propstatus = models.CharField(choices=d,default='a',max_length=10)
    propdoc = models.FileField(upload_to='Attachments/')
    propsoldto = models.CharField(max_length=200,null=True,blank=True)
    propown = models.CharField(max_length=200,default='Default Owner')
    propprevown = models.CharField(max_length=200,default='Owner')
    pown = models.ForeignKey(User,on_delete=models.CASCADE)


