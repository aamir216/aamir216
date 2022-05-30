from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from .models import Prediction
import socket
from bs4 import BeautifulSoup
import csv
from csv import writer
import string
from io import StringIO
import requests
import datetime
from datetime import date

# def index(request):
#     return HttpResponse('HELLO WORLD')
def index(request):
    
    preds=Prediction.objects.all().order_by('-volume')
        # GET LIVE VOLUME

    main = requests.get('https://www.psx.com.pk/')
    soup = BeautifulSoup(main.text, 'html.parser')

    status = soup.find("tr").find_next('td', string="Market Status").find_next('td').text.strip()
    # status = soup.find("td").find_next('p').text.strip().replace('Status: ', '')
    ksevolume = soup.find("tr").find_next('td', string="Current Index").find_next('td').text.strip()
    # ksevolume = float(ksevolume)
    # ksevolume=("{:,}".format(ksevolume))   #SET FORMAT LIKE 333,33.99
    
    current_point = soup.find("tr").find_next('td', string="Change").find_next('td', id='cahnge').text.strip()
    
    current_point_percentage = soup.find("tr").find_next('td', string="Percent Change").find_next('td', id='percentchange').text.strip()
     
    main = requests.get('https://www.psx.com.pk/market-summary/')
    soup = BeautifulSoup(main.text, 'html.parser')

    Loadedtime = soup.find('div', class_='col-sm-12 inner-content-table').find_next('h4').text.strip()
    hrs=(Loadedtime[11:-6])
    hrs = int(hrs)
    # ksevolume = soup.find("div", class_="col-xs-6").find_next('h3', string="KSE100").find_next("h4").text.strip()
    # 

    currentmarkestatus = '('+status+')  KSE100 Volume: '+ksevolume+ '    ('+current_point+' / '+current_point_percentage+')'

    now = datetime.datetime.now()
    day=now.strftime("%A")

    print(day)
    print(hrs)
    if day == 'Friday':
        if hrs >= 16:
            heading=' Listed For Next Day Profit'
            time="evening"
        elif hrs < 16:
            time="morning"
            heading=' Listed For Short Time Profit'
    else:
        if hrs >= 15:
            heading=' Listed For Next Day Profit'
            time="evening"
        elif hrs < 15:
            time="morning"
            heading=' Listed For Short Time Profit'
        
    context = {
        'preds': preds,
        'currentmarkestatus':currentmarkestatus,        
        'heading':heading,
        'Loadedtime':Loadedtime,
        'time': time,
    }
    return render(request, 'prediction/index.html',context)

# def thanks(request):
#     if request.method == 'POST':
#         like = Response()
#         like.save()
    
#     return render(request, 'prediction/thanks.html')