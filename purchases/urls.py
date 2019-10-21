from django.conf.urls import url
from .views import checkout, order_history

urlpatterns = [
    url(r'^$', checkout, name='checkout'),
    url(r'^$', order_history, name='order_history'),
    
]