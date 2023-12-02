from django.db import models
from django.core.validators import FileExtensionValidator


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

