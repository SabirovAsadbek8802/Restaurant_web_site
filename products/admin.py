from django.contrib import admin
from .models import (Category, Product, ProductImage, ProductInfo, ProductDetail, ProductReview)

admin.site.register(Category)
admin.site.register(ProductImage)
admin.site.register(ProductInfo)
admin.site.register(ProductDetail)
admin.site.register(ProductReview)


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0


class ProductDetailInline(admin.TabularInline):
    model = ProductDetail
    extra = 0


class ProductInfoInline(admin.TabularInline):
    model = ProductInfo
    extra = 0


class ProductReviewInline(admin.TabularInline):
    model = ProductReview
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline, ProductDetailInline, ProductInfoInline, ProductReviewInline]
    list_per_page = 100
