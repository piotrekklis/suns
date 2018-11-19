from django.shortcuts import render
from django.http import HttpResponse
from scraper.models import Currency, CurrencyFeed
from datetime import datetime, timezone
from dateutil import parser
import xmltodict
import urllib.request
from django.db import IntegrityError
# REST
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from scraper.serializers import UserSerializer, GroupSerializer, CurrencyFeedSerializer, CurrencySerializer

from django_filters import rest_framework as filters

def index(request):

    objectsList = []
    linksToParse = []

    links = CurrencyFeed.objects.all()
    for i in links:
        linksToParse.append(i.link)

    for link in linksToParse:
        # source = CurrencyFeed.objects.get(id = 1).link
        # get xml
        with urllib.request.urlopen(link) as f:
            data = f.read()

        # xml to dict
        data = xmltodict.parse(data)
        counter = 0

        while counter <= len(data['rdf:RDF']['item']) - 1:
            # title
            title = data['rdf:RDF']['item'][counter]['title']['#text']
            objectsList.append(' TITLE : ')
            objectsList.append(title)
            # link
            link = data['rdf:RDF']['item'][counter]['link']
            objectsList.append(' LINK : ')
            objectsList.append(link)
            # description
            description = data['rdf:RDF']['item'][counter]['description']['#text']
            objectsList.append(' DESCRIPTION : ')
            objectsList.append(description)
            # date
            datetime_object = data['rdf:RDF']['item'][counter]['dc:date']
            datetime_object = parser.parse(datetime_object)
            objectsList.append(' DATE : ')
            objectsList.append(datetime_object)
            # currency_value
            currency_value = data['rdf:RDF']['item'][counter]['cb:statistics']['cb:exchangeRate']['cb:value']['#text']
            objectsList.append(' VALUE : ')
            objectsList.append(currency_value)
            # baseCurrency
            baseCurrency = data['rdf:RDF']['item'][counter]['cb:statistics']['cb:exchangeRate']['cb:baseCurrency']['#text']
            objectsList.append(' BC : ')
            objectsList.append(baseCurrency)
            # targetCurrency
            targetCurrency = data['rdf:RDF']['item'][counter]['cb:statistics']['cb:exchangeRate']['cb:targetCurrency']
            objectsList.append(' TC : ')
            objectsList.append(targetCurrency)

            currencyObject = Currency(title = title, link = link, description = description, publication_date_time = datetime_object, currency_value = currency_value, baseCurrency = baseCurrency, targetCurrency = targetCurrency)
            try:
                currencyObject.save()
            except IntegrityError:
                pass

            counter = counter + 1

    return HttpResponse(objectsList)

# viewSets
class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    http_method_names = ['get']

class GroupViewSet(viewsets.ModelViewSet):

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    http_method_names = ['get']

class CurrencyFeedViewSet(viewsets.ModelViewSet):

    queryset = CurrencyFeed.objects.all()
    serializer_class = CurrencyFeedSerializer
    http_method_names = ['get', 'post']

class CurrencyViewSet(viewsets.ModelViewSet):

    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    http_method_names = ['get']

class CurrencyFilter(filters.FilterSet):

    class Meta:
        model = Currency
        fields = ['targetCurrency']

class FilteredCurrencyViewSet(viewsets.ModelViewSet):

    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = CurrencyFilter
    http_method_names = ['get']
