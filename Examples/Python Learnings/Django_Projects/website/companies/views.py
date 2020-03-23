# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Stocks
from .serializers import StocksSerializer


# Create your views here.
# Lists all stocks or create a new one
# stocks/
class StockList(APIView):
    def get(self, request):
        stocks = Stocks.objects.all()
        serializer = StocksSerializer(stocks, many=True)
        return Response(serializer.data)

    def post(self):
        pass
