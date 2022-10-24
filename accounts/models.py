from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser
from import_export.admin import ImportExportModelAdmin

# Create your models here.
class User(AbstractUser):
    is_enduser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    
class Enduser(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=254)
    mobile_number = models.CharField(max_length=254)
    email = models.CharField(max_length=254)
    
    def __str__(self):        
        return self.first_name
    
class ticker(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)    
    stock_ticker =models.CharField(max_length=254)
    dividend_type = models.CharField(max_length=254,default="Not Declared")
    dividend_percetage =models.CharField(max_length=254,default="Not Declared")
    stock_record_date = models.CharField(max_length=254,default="Not Declared")
    stock_announcement_date =models.CharField(max_length=254,default="Not Declared")
    ex_dividend_date = models.CharField(max_length=254,default="Not Declared")
    mail_sent = models.BooleanField(default=False)
    
    def __str__(self):        
        return self.stock_ticker

class nse_bse_stocks(models.Model):
    symbol =models.CharField(max_length=254)
    name_of_company =models.CharField(max_length=254)
    series =models.CharField(max_length=254)
    date_of_listing =models.CharField(max_length=254)
    paid_up_value =models.CharField(max_length=254)
    market_lot =models.CharField(max_length=254)
    isin_number =models.CharField(max_length=254)
    face_value =models.CharField(max_length=254)
    
    def __str__(self):
                
        return self.symbol

class nse_bse_dividend_alerts(models.Model):
    Stock_ticker =models.CharField(max_length=254)
    dividend_type =models.CharField(max_length=254,default="Not Declared")
    dividend_precentage = models.CharField(max_length=254,default="Not Declared")
    date_announcement =models.CharField(max_length=254,default="Not Declared")
    date_record = models.CharField(max_length=254,default="Not Declared")
    ex_dividend_date = models.CharField(max_length=254,default="Not Declared")
    face_value =models.CharField(max_length=254,null=True)
    
    def __str__(self):        
        return self.Stock_ticker
    
    class Meta:
        ordering = ('-date_announcement',)
    
class MultipleImage(models.Model):
    images = models.FileField()
    
  