from django.db import models
from django.core.validators import FileExtensionValidator, MinValueValidator, MaxValueValidator
from users.models import CustomUser as User


class Category(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='media/',
                              validators=[FileExtensionValidator(allowed_extensions=["jpg", "png"])])

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.RESTRICT, related_name='product')
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    discount = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    description = models.TextField()
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    motto = models.TextField()

    def __str__(self):
        return self.name


class ProductDetail(models.Model):
    products = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='detail')
    product_description = models.TextField()

    def __str__(self):
        return self.products.name


class ProductImage(models.Model):
    products = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='media/',
                              validators=[FileExtensionValidator(allowed_extensions=["jpg", "png"])])

    def __str__(self):
        return self.products.name


class ProductReview(models.Model):
    products = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='review')
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    comment = models.TextField()

    def __str__(self):
        return self.products.name


class ProductInfo(models.Model):
    products = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='info')
    key = models.CharField(max_length=200)
    value = models.CharField(max_length=200)

    def __str__(self):
        return '%s - %s' % (self.products.name, self.key)
