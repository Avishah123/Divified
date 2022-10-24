import imp
from.serializers import *
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render, redirect, get_object_or_404, reverse
from accounts import models
from accounts.models import *


@api_view(('GET',))
def get_api(request):
    stocks = nse_bse_dividend_alerts.objects.all()
    serializer = stock_ticker(stocks,many=True)
    return Response(serializer.data)
