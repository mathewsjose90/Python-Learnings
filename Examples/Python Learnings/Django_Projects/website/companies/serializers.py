from rest_framework import serializers
from .models import Stocks


class StocksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stocks
        # fields = ('ticker', 'volume')
        fields = '__all__'
