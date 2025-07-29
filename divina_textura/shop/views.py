from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Category, Subcategories
from .forms import AddToCartForm
import pandas as pd

def add_to_cart_view_pandas_version(request, slug):
    try:
        df = pd.read_csv("produse_salvate.csv", index_col=0)
    except:
        df = pd.DataFrame({"produse": []})
    df.loc[len(df)] = slug
    df.to_csv("produse_salvate.csv")
    return redirect("cart_url")

def home_view(request):
    products = Product.objects.all()
    form = AddToCartForm()
    categories = Category.objects.all()
    context = {
        "products": products,
        "form": form,
        "categories": categories,
    }
    return render(request, 'all_products.html', context)

def product_details_view(request, slug):
    product = get_object_or_404(Product, slug=slug)
    categories = Category.objects.all()
    return render(request, 'product_details.html', {
        'product': product,
        'categories': categories,
    })

def all_categories_view(request):
    categories = Category.objects.all().prefetch_related('subcategories')
    return render(request, 'all_categories.html', {'categories': categories})

def category_details_view(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(categories=category)
    categories = Category.objects.all()
    return render(request, 'category_details.html', {
        'category': category,
        'products': products,
        'categories': categories,
    })

def subcategory_details_view(request, parent_slug, sub_slug):
    parent_category = get_object_or_404(Category, slug=parent_slug)
    subcategory = get_object_or_404(Subcategories, slug=sub_slug, parent_category=parent_category)
    products = Product.objects.filter(subcategory=subcategory, categories=parent_category)
    categories = Category.objects.all()
    return render(request, 'subcategory_details.html', {
        'parent_category': parent_category,
        'subcategory': subcategory,
        'products': products,
        'categories': categories,
    })
