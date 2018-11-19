from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class Currency(models.Model):
    title = models.CharField(max_length = 200)
    link = models.CharField(max_length = 200)
    description = models.CharField(max_length = 500)
    publication_date_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    currency_value = models.DecimalField(max_digits = 19, decimal_places = 4)
    baseCurrency = models.CharField(max_length = 10)
    targetCurrency = models.CharField(max_length = 10)

    class Meta:
        unique_together = ('publication_date_time', 'targetCurrency')

class CurrencyFeed(models.Model):
    name = models.CharField(max_length = 100, unique = True)
    link = models.CharField(max_length = 200, unique = True)
