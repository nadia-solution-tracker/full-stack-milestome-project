from django.conf.urls import url,include
from reviews.views import add_review

urlpatterns = [
   url(r'^product/(?P<product_id>[0-9]+)/add_review/$', add_review, name='add_review'),
]