from django.conf.urls import url,include
from products.views import all_products, product_detail

urlpatterns = [
    url(r'^$', all_products, name='products'),
    url(r'^product/(\d+)', product_detail, name='product_detail')
]
