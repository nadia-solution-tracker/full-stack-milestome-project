from django.conf.urls import url,include
from products.views import all_products, product_detail, show_products_category
from reviews.views import add_review

urlpatterns = [
    url(r'^$', all_products, name='products'),
    url(r'^product/(\d+)', product_detail, name='product_detail'),
    url(r'^(?P<category_name>[\w.@+-]+)', show_products_category, name='show_products_category'),
    # url(r'^(?P<author_firstname>[\w.@+-]+)', show_products_author, name='show_products_author'),
    url(r'^/products/<int:pk>/reviews/', add_review, name='add_review'),
]
