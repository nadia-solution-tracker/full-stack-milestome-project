from django.db import models

# Create your models here.

class Category(models.Model):
    """Model class for Category"""
    name = models.CharField(max_length=254,default='') 
    
    def __str__(self):
        return self.name
    
    
class Author(models.Model):
    """Model class for Author"""
    firstname = models.CharField(max_length=254,default='')
    lastname = models.CharField(max_length=254,default='')
    
    def __str__(self):
        return self.firstname + " " + self.lastname
    
class Product(models.Model):
    """ Model class for Books """
    name = models.CharField(max_length=254,default='')
    description = models.TextField()
    publication_year = models.IntegerField(null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE,null= False)
    price = models.DecimalField(max_digits=6,decimal_places=2)
    image = models.ImageField(upload_to='images')
    instock = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,null= False)
    
    def __str__(self):
        return self.name
    