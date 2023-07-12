from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    Product_name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    image = models.ImageField(upload_to="shop/images", default="")
    description = models.CharField(max_length=300, default="")


    def __str__(sel):
        return sel.Product_name