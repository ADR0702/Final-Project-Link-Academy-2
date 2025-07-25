from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Category
from .forms import AddToCartForm
import pandas as pd

# ✅ Adăugare produs în coș (cu CSV + pandas)
def add_to_cart_view_pandas_version(request, slug):
    print("Ar trebui adaugat in cos..", slug)

    try:
        df = pd.read_csv("produse_salvate.csv", index_col=0)
    except:
        df = pd.DataFrame({"produse": []})

    df.loc[len(df)] = slug
    df.to_csv("produse_salvate.csv")

    return redirect("cart_url")


# ✅ Pagina principală cu toate produsele
def home_view(request):
    products = Product.objects.all()
    form = AddToCartForm()
    context = {
        "products": products,
        "form": form,
    }
    return render(request, 'all_products.html', context)


# ✅ Pagină detaliu produs (poți completa mai târziu)
def product_details_view(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'product_details.html', {'product': product})



# ✅ Listă categorii (Women, Men, Kids)
def all_categories_view(request):
    categories = Category.objects.all()
    context = {
        "categories": categories
    }
    return render(request, 'all_categories.html', context)


# ✅ Detalii categorie + produse asociate (ManyToMany fix)
def category_details_view(request, slug):
    category = get_object_or_404(Category, slug=slug)
    
    # Aici folosim ManyToManyField corect:
    products = Product.objects.filter(categories=category)

    context = {
        "category": category,
        "products": products
    }
    return render(request, 'category_details.html', context)
