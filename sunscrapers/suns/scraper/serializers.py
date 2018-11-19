from django.contrib.auth.models import User, Group
from scraper.models import CurrencyFeed, Currency
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Group
        fields = ('url', 'name')

class CurrencyFeedSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = CurrencyFeed
        fields = ('name', 'link')

class CurrencySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Currency
        fields = ('currency_value', 'targetCurrency', 'publication_date_time')
