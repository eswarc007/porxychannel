# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import viewsets
from .models import  proxies
from .serializers import ProxySerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Count


class countryView(APIView):
    permission_classes = (IsAuthenticated, )
    def get(self, request):
        queryset = proxies.objects.all()
        if len(self.request.query_params) ==1 and 'format' in self.request.query_params:
            queryset = proxies.objects.values('country').distinct().annotate(proxies_count=Count('country'))
            return Response ({'countries_list' : queryset})
        country = self.request.query_params.get('country', None)
        print country
        if country is not None:
            countryqueryset = queryset.filter(country=country).values('country').annotate(proxies_count=Count('country'))
        try:
#             return queryset
            return Response({countryqueryset})
        except:
            return Response({})

class cityView(APIView):
    permission_classes = (IsAuthenticated, )
    def get(self, request):
        queryset = proxies.objects.all()
        if len(self.request.query_params) ==1 and 'format' in self.request.query_params:
            queryset = proxies.objects.values('city', 'country').distinct().annotate(proxies_count=Count('city'))
            return Response ({'City_list' : queryset})
        city = self.request.query_params.get('city', None)
        if city is not None:
            cityqueryset = queryset.filter(city=city).values('city', 'country').annotate(proxies_count=Count('proxy'))
        try:
#             return queryset
            return Response({cityqueryset})
        except:
            return Response({})
class RegionView(APIView):
    permission_classes = (IsAuthenticated, )
    def get(self, request):
        queryset = proxies.objects.all()
        if len(self.request.query_params) ==1 and 'format' in self.request.query_params:
            queryset = proxies.objects.values('region', 'city', 'country').distinct().annotate(proxies_count=Count('region'))
            return Response ({'Region_list' : queryset})
        region = self.request.query_params.get('region', None)
        if region is not None:
            regionqueryset = queryset.filter(region=region).values('region','city', 'country').annotate(proxies_count=Count('proxy'))
        try:
#             return queryset
            return Response({regionqueryset})
        except:
            return Response({})


class ProxyViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = proxies.objects.all()
    serializer_class = ProxySerializer
    def get_queryset(self):
        if len(self.request.query_params) ==1 and 'format' in self.request.query_params:
            return {}
        queryset = proxies.objects.all()
        sourceid = self.request.query_params.get('sid', None)
        if sourceid is not None:
            queryset = queryset.filter(sourceid=sourceid)
        city = self.request.query_params.get('city', None)
        if city is not None:
            queryset = queryset.filter(city=city)
        region = self.request.query_params.get('region', None)
        if region is not None:
            queryset = queryset.filter(region=region)
        country = self.request.query_params.get('country', None)
        if country is not None:
            queryset = queryset.filter(country=country)
        countrycode = self.request.query_params.get('countrycode', None)
        if countrycode is not None:
            queryset = queryset.filter(countrycode=countrycode)
        source =  self.request.query_params.get('source', None)
        if source is not None:
            kwargs = {source: 1}
            queryset = queryset.filter(**kwargs)
        ports = self.request.query_params.get('port', None)
        if ports is not None:
            queryset = queryset.filter(ports=ports)
        random = self.request.query_params.get('random', None)
        try:
            if random == 'false':
                return queryset
            else:
                return queryset.random()
        except:
            return {}