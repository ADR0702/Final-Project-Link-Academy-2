from django.shortcuts import render, redirect

# Create your views here.
from .models import Product, Category

from .forms import AddToCartForm

import pandas as pd



def add_to_cart_view_pandas_version(request, slug):
	print("Ar trebui adaugat in cos..", slug)

	### LOGICA de cart
	try:
		df = pd.read_csv("produse_salvate.csv", index_col=0)
	except:
		df = pd.DataFrame({"produse":[]})

	df.loc[len(df)] = slug
	df.to_csv("produse_salvate.csv")

	

	return redirect("cart_url")




# from cart.views import CartLogic
# cart_logic = CartLogic(request)
# "cart":cart_logic


def home_view(request):

	products = Product.objects.all()
	form = AddToCartForm()
	
	context = {
		"products": products,
		"form" : form,
	}
	
	return render(request, 'all_products.html', context)

def product_details_view(request):
	context = {}
	return render(request, 'product_details.html', context)

def all_categories_view(request):
	categories = Category.objects.all()
	context = {
		"categories":categories
	}
	return render(request, 'all_categories.html', context)

def category_details_view(request, slug):
	category_details = Category.objects.filter(slug=slug).first()
	if not category_details:
		return redirect("categories_url")
	

	products = Product.objects.filter(category=category_details)

	context = {"category": category_details,
			"products":products}
	
	return render(request, 'category_details.html', context)
