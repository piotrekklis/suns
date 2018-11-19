from django.urls import path

from . import views

from django.conf.urls import url, include
from rest_framework import routers
from scraper import views
from django.conf import settings
from django.conf.urls.static import static

from . import views as local_view
from rest_framework.authtoken import views as rest_framework_views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'currencyfeeds', views.CurrencyFeedViewSet)
router.register(r'currency', views.CurrencyViewSet)
router.register(r'filteredcurrencies', views.FilteredCurrencyViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^get_auth_token/$', rest_framework_views.obtain_auth_token, name='get_auth_token'),
]
