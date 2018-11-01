from rest_framework import serializers
from .models import  proxies

class ProxySerializer(serializers.ModelSerializer):
    class Meta:
        model = proxies
        fields = ('id', 'sourceid', 'proxy', 'city', 'region', 'country', 'countrycode', 'ports')
        
# class CountrySerializer(serializers.ModelSerializer):
#     count = serializers.SerializerMethodField()
#     class Meta:
#         model = proxies
#         fields = ('country','count',)
#         read_only_fields = ('count',)
#         def get_days_since_joined(self, obj):
#             return {"country" : obj.country, 'count' : obj.count}