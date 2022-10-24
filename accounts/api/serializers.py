from rest_framework import serializers

class stock_ticker(serializers.Serializer):
    Stock_ticker = serializers.CharField()
    dividend_type = serializers.CharField()
    dividend_precentage = serializers.CharField() 
    date_announcement = serializers.CharField()
    date_record =serializers.CharField()
    ex_dividend_date =serializers.CharField()
    