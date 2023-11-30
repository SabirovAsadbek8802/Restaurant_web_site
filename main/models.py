from django.db import models
from django.core.validators import FileExtensionValidator


# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='media/',
                              validators=[FileExtensionValidator(allowed_extensions=["jpg", "svg", "png", "ico"])])
    def __str__(self):
        return self.name


class Menu_item(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    description = models.TextField()
    price = models.DecimalField(max_digits=4, decimal_places=2)
    discount_price = models.DecimalField(max_digits=4,decimal_places=2)
    image = models.ImageField(upload_to='media/',
                              validators=[FileExtensionValidator(allowed_extensions=["jpg", "svg", "png", "ico"])])
    like = models.IntegerField()
    cart = models.ForeignKey("Cart", on_delete=models.DO_NOTHING)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Cart(models.Model):
    name = models.CharField(max_length=150)
    discount_price = models.IntegerField()
    image = models.ImageField(upload_to='media/',
                              validators=[FileExtensionValidator(allowed_extensions=["jpg", "svg", "png", "ico"])])

    def __str__(self):
        return self.name

    @classmethod
    def total_all_products(cls, request):
        data =cls.objects.all().select_related('menu_item')
        if Menu_item.status == False:
            return None
        else:
            return sum(i.discount_price for i in data)

