from django.contrib import admin
from .models import Product, Category, Subcategories, ProductImage
from .forms import ProductImageInlineFormSet  # folosim formset, nu form


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
    max_num = 10
    formset = ProductImageInlineFormSet  


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


@admin.register(Subcategories)
class SubcategoryModelAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}
