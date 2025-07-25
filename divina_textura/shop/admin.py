from django.contrib import admin
from .models import Product, Category, Subcategories, ProductImage


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
    max_num = 10  # maxim 10 imagini


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "slug", "price")
    search_fields = ("name", "description", "slug", "price")
    prepopulated_fields = {"slug": ("name",)}
    inlines = [ProductImageInline]  


@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "slug", "id",)
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Subcategories)
