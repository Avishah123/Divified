import re
from xml.etree.ElementTree import XML
from django.shortcuts import render
from time import timezone
from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.views.generic import CreateView
from django.contrib.auth import login
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.mail import send_mail
import csv
from django.http import HttpResponse
from django.contrib import auth
from .models import *
from django.template.loader import render_to_string
import datetime

from django.forms import ValidationError
from django.contrib import messages
# Create your views here.
from django.contrib.auth.decorators import login_required
import pandas as pd 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import schedule
import time
from bs4 import BeautifulSoup
import time
from datetime import datetime
import csv
import pandas as pd
from selenium.webdriver.support.ui import Select
import psycopg2
import pandas as pd
from sqlalchemy import create_engine
import numpy as np
from django.shortcuts import render
from django.views.generic import View
   
from rest_framework.views import APIView
from rest_framework.response import Response
# we have to use the USER table to access the id of the user and not the Enduser

def form_rendering_test(request):
    languages  = nse_bse_stocks.objects.all()
    return render(request,'forms/test.html',{"languages":languages})

def scraper(stock_name):
    url = 'https://www.moneycontrol.com/stocks/marketinfo/dividends_declared/index.php'

    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    chrome_browser = webdriver.Chrome('accounts/chromedriver.exe',options=options)

    chrome_browser.get(url)
    ddelement= Select(chrome_browser.find_element_by_xpath('//*[@id="sel_year"]'))
    ddelement.select_by_value('2022')

    go_button = chrome_browser.find_element_by_xpath('//*[@id="bonus_frm"]/div/table/tbody/tr/td[3]/input')
    go_button.click()

    time.sleep(10)

    html = chrome_browser.page_source

    mc = pd.read_html(html)
    xm = mc[1:]
    pritesh = np.squeeze(xm,axis= 0)
    df = pd.DataFrame(pritesh)
    # print(df)
    x = str(stock_name)
    test =df.loc[df[0] == x]
    if(test.empty == False):
        print(test)
        print('before renaming')
        print(list(test.columns))
        test.columns = ['Stock_ticker', 'dividend_type', 'dividend_precentage','date_announcement','date_record','ex_dividend_date']
        x= test.to_dict(orient='records')
        print(x)        
        return x
        
    else :
        print('no dividend declared')
        return None

class organizer(CreateView):
    model = User
    form_class = EnduserSignUpForm
    template_name = 'dashboard/register1.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)       

        return redirect('home')

@login_required
def event_view(request):
    languages  = nse_bse_stocks.objects.all()
    context ={
        "languages":languages,
    }
    # create object of form
    form = stockform(request.POST or None, request.FILES or None)
    # check if form data is valid
    if form.is_valid():
        # save the form data to model
        
        form.save(request)
        messages.success(request, "Entry Success")
        return redirect('dashboard')
  
    context['form']= form
    
    return render(request, "dashboard/add_stock.html", context)


def home(request): 
    print(1)
    return render(request,'landing.html')

def current_user(request):
    x = request.user
    return x


def dash_meta(request):
    
    x =nse_bse_dividend_alerts.objects.all().order_by('-date_announcement')
    stock_ticker = ticker.objects.filter(user=request.user)
          
    for y in stock_ticker:
        for i in x:
            if(y.stock_ticker.lower() == i.Stock_ticker.lower()):
                print('Ticker Matched'+i.Stock_ticker)
                y=ticker.objects.get(user=request.user,stock_ticker=y.stock_ticker)
                print(y)
                y.dividend_type=i.dividend_type
                y.dividend_percetage=i.dividend_precentage
                y.stock_record_date=i.date_record
                y.stock_announcement_date=i.date_announcement
                print(y.stock_announcement_date)
                y.ex_dividend_date=i.ex_dividend_date
                y.save() 
                break

@login_required
def dashboard(request):
    dash_meta(request)
    stock_ticker = ticker.objects.filter(user=request.user).order_by('-id')  
    user_details = Enduser.objects.filter(user=request.user)
    stock_count = ticker.objects.filter(user=request.user).count()
    print(stock_count)
   
    # refresh_db()
    context = {        
        'stock_ticker' : stock_ticker,
        'user_details':user_details,  
        'stock_count':stock_count,
              
    }
    return render(request,'dashboard/index.html',context)

def refresh_db():
    url = 'https://www.moneycontrol.com/stocks/marketinfo/dividends_declared/index.php'

    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    chrome_browser = webdriver.Chrome('accounts/chromedriver.exe',options=options)
    chrome_browser.get(url)
  

    go_button = chrome_browser.find_element_by_xpath('//*[@id="bonus_frm"]/div/table/tbody/tr/td[3]/input')
    go_button.click()

    time.sleep(10)

    html = chrome_browser.page_source

    mc = pd.read_html(html)

    # print(mc)

    xm = mc[1:]
    pritesh = np.squeeze(xm,axis= 0)
    df = pd.DataFrame(pritesh)
    # print(df)
    df.columns = ['Stock_ticker', 'dividend_type', 'dividend_precentage','date_announcement','date_record','ex_dividend_date']
    df.drop([0,1], axis=0, inplace=True)
    print(df)
    x= df.to_dict(orient='records')
    nse_bse_dividend_alerts.objects.all().delete()
    print(x)
    for i in x:
            print(i)
            price =i['Stock_ticker']
            dividend_type = i['dividend_type']
            dividend_precentage = i['dividend_precentage']
            date_announcement = i['date_announcement']
            date_record = i['date_record']
            ex_dividend_date = i['ex_dividend_date']
            
            y= nse_bse_dividend_alerts(Stock_ticker=price,dividend_type=dividend_type,dividend_precentage=dividend_precentage,date_announcement=date_announcement,date_record=date_record,ex_dividend_date=ex_dividend_date)
            y.save()
            
            
    print(price)
    print(dividend_type)
    print(date_record)
    print(date_announcement)
    print(dividend_precentage)
    print(ex_dividend_date)
    
    
def delete(request,stock_id):
    item = ticker.objects.get(pk=stock_id)
    item.delete()
    messages.success(request,("stock has been removed succesfully"))
    return redirect('dashboard')

def delete_stock(request):
    ticker = ticker.objects.all()
    return render(request,'delete_stock.html',{'ticker' : ticker})


def dash_index(request):
    # x=nse_bse_dividend_alerts.objects.all()
    x =nse_bse_dividend_alerts.objects.all().order_by('-date_announcement')
    print(x)
    for i in x:
        if(i.Stock_ticker == 'IEX'):
            print(i.date_announcement)
    
    return render(request,'dashboard/index.html')

def dash_login(request):
    return render(request,'dashboard/login1.html')

def dash_register(request):
    return render(request,'dashboard/register1.html')

def new_landing(request):
    return render(request,'landing.html')

class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'charts.html')
    
class ChartData(APIView):
    authentication_classes = []
    permission_classes = []
   
    def get(self, request, format = None):
        labels = [
            'January',
            'February', 
            'March', 
            'April', 
            'May', 
            'June', 
            'July'
            ]
        chartLabel = "my data"
        chartdata = [0, 10, 5, 2, 20, 30, 45]
        data ={
                     "labels":labels,
                     "chartLabel":chartLabel,
                     "chartdata":chartdata,
             }
        return Response(data)

from django.shortcuts import render
from .models import MultipleImage


def upload(request):
    if request.method == "POST":
        images = request.FILES.getlist('images')
        for image in images:
            MultipleImage.objects.create(images=image)
    images = MultipleImage.objects.all()
    return render(request, 'images.html', {'images': images})

def analyser_view(request):
    languages  = MultipleImage.objects.all()    
    context ={
        "languages":languages,
    }
    # create object of form
    form = stockform(request.POST or None, request.FILES or None)
    # check if form data is valid
    if form.is_valid():
        # save the form data to model
        
        form.save(request)
        messages.success(request, "Entry Success")
        return redirect('dashboard')
  
    context['form']= form
    
    return render(request, "dashboard/add_stock.html", context)

def upload_view(request):    
    images = MultipleImage.objects.all()
    return render(request, 'dividend_analysis.html', {'images': images})

# Take all the rows with the ticker name tcs and show all the queries 
def test_history(request):
    queryset = nse_bse_dividend_alerts.objects.filter(Stock_ticker='TCS')
    for i in queryset:
        print(i.date_announcement)
    print(queryset)
    return render(request,'history.html')

def hist_view(request,Stock_ticker):
    stock_ticker = nse_bse_dividend_alerts.objects.filter(Stock_ticker=Stock_ticker)
    for i in stock_ticker:
        print(i.date_announcement)
        
    context ={
        "stock_ticker":stock_ticker,
    }    
    
    return render(request,'dashboard/history.html',context)

# ticker table and alert table to be linked

def face_con(request):
    x =nse_bse_dividend_alerts.objects.all()
    y= nse_bse_stocks.objects.all()
    
          
    for i in x:
        for z in y:
            if(z.symbol.lower().replace(" ","") == i.Stock_ticker.lower().replace(" ","") or z.name_of_company.lower().replace(" ","") == i.Stock_ticker.lower().replace(" ","") ):
                print('Ticker Matched'+z.symbol)
                xy = nse_bse_dividend_alerts.objects.filter(Stock_ticker=i.Stock_ticker).update(face_value=z.face_value)
                
    return render(request,'dashboard/history.html')