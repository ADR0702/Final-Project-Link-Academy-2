from django.contrib import admin

# Register your models here.
from .models import Product, Category

# admin.site.register(Product)


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ( "name", "description", "slug", "price")
    search_fields =( "name", "description", "slug", "price")
    prepopulated_fields = {"slug" : ("name",)}


# admin.site.register(Category)


@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ( "name", "description", "slug", "id",)
    search_fields = ("name",)
    prepopulated_fields = {"slug" : ("name",)}


