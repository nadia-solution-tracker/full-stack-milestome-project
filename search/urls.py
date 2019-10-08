from django.conf.urls import url
from search.views import search_products

urlpatterns = [
    url(r'^$',search_products, name='search')]