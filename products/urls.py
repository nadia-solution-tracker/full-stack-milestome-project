from django.conf.urls import url,include
from products.views import all_products, product_detail, show_products

urlpatterns = [
    url(r'^$', all_products, name='products'),
    url(r'^product/(\d+)', product_detail, name='product_detail'),
    url(r'^(?P<category_name>[\w.@+-]+)', show_products, name='show_products'),
]
