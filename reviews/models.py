from django.db import models
from products.models import Product
from django.contrib.auth.models import User

# Create your models here.
class Review(models.Model):
    RATING_CHOICES = (
	(0, '0'),
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)
    comment = models.CharField(max_length=254, default='')
    rating = models.IntegerField(choices=RATING_CHOICES, default=0)
