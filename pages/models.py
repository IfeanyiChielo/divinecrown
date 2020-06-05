from django.db import models
from datetime import date
class Employee(models.Model):
    fullname = models.CharField(max_length=100)
    emp_code = models.CharField(max_length=3)
    mobile= models.CharField(max_length=15)
    position= models.CharField(max_length=15)

class Staffrec(models.Model):
    staff_id = models.CharField(max_length=5,primary_key=True)
    fullname = models.CharField(max_length=35)
    sex = models.CharField(max_length=7)
    email = models.EmailField()
    address = models.CharField(max_length=100)  
    mobile= models.CharField(max_length=15)
    position= models.CharField(max_length=30)
    department = models.CharField(max_length=25)
# class Meta:  
#     db_table = "staffrec"  

class Soapprod (models.Model):
    id = models.AutoField(primary_key=True)
    Serial_White_Guava                  = models.PositiveIntegerField()
    Serial_White_Premium                = models.PositiveIntegerField()
    Soft_Flower_Body_Wash               = models.PositiveIntegerField()
    Soft_Flower_Fresh                   = models.PositiveIntegerField()
    Soft_Flower_Orange_Lightening       = models.PositiveIntegerField()
    Soft_Flower_Carot_Lightening        = models.PositiveIntegerField()
    Soft_Flower_Papaya_Extract          = models.PositiveIntegerField()
    Soft_Flower_Extra_Lightening        = models.PositiveIntegerField()
    Serial_White_Papaya_4in1            = models.PositiveIntegerField()
    date                                = models.DateField(default = date.today)
   
    def __str__(self):
        return self.serial_white_guava
 
class Creamprod (models.Model):
    id = models.AutoField(primary_key=True)
    Serial_White_ExLM     = models.PositiveIntegerField() 
    Serial_White_Gold_SWM = models.PositiveIntegerField()
    Soft_Flower_LL        = models.PositiveIntegerField()
    Soft_Flower_FC        = models.PositiveIntegerField()
    date                  = models.DateField(default = date.today)


from django.contrib.auth.models import User
# Create your models here.
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
def __str__(self):
  return self.user



class Soapsales (Soapprod):
    SOAP_MARKETER_STATUS = (
        ('M', 'Marketers'),
        ('D', 'Distributor'),
        ('A', 'Distributor_B'),
        ('B', 'Distributor_C'),
    )    
    soap_marketer_status = models.CharField(max_length=1, choices=SOAP_MARKETER_STATUS)

class Creamsales (Creamprod):
    CREAM_MARKETER_STATUS = (
        ('A', 'Groupa'),
        ('B', 'Groupb'),
        ('C', 'Groupc'),
    )
    cream_marketer_status = models.CharField(max_length=1, choices=CREAM_MARKETER_STATUS)

class Staffinfo (models.Model):
    staff_id = models.CharField(max_length=5)
    staff_name = models.CharField(max_length=7)