from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Category, Subcategories
from .forms import AddToCartForm, CustomUserCreationForm
import pandas as pd
from django.db.models import Q
from django.contrib.auth.views import LoginView
from django.contrib.auth import login, authenticate
from django.shortcuts import render

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        terms_accepted = request.POST.get('terms') == 'on'
        gdpr_accepted = request.POST.get('gdpr') == 'on'

        if not terms_accepted:
            form.add_error(None, "You must accept the Terms and Conditions.")
        if not gdpr_accepted:
            form.add_error(None, "You must accept the GDPR policy.")

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('registration_success')  # pagina cu mesaj succes înregistrare
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

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

    # poți selecta doar produsele "featured" sau cele mai noi
    featured_products = Product.objects.all()[:6]

    context = {
        "products": products,
        "featured_products": featured_products,
        "form": form,
        "categories": categories,
    }
    return render(request, 'home.html', context)

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

def product_search(request):
    query = request.GET.get('q')
    results = []

    if query:
        results = Product.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )

    return render(request, 'shop/search_results.html', {
        'query': query,
        'results': results,
    })
def terms_conditions_view(request):
    return render(request, 'terms_conditions.html')

def gdpr_view(request):
    return render(request, 'gdpr.html')
def registration_success_view(request):
    return render(request, 'registration_success.html')
def delivery_returns_view(request):
    return render(request, 'shop/deliveryreturns.html')