from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "categorie"

class Subcategories(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    parent_category = models.ManyToManyField(Category, related_name="subcategories")

    def __str__(self):
        return f"{self.parent_category.name} - {self.name}"

class Product(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="product_images")
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    # MODIFICAT:
    categories = models.ManyToManyField(Category)
    subcategory = models.ForeignKey(Subcategories, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='product_images')

    def __str__(self):
        return f"Imagine pentru {self.product.name}"
