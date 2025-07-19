from django.shortcuts import render, redirect
from  shop.models import Product 
# Create your views here.

from shop.forms import IncreaseForm, DecreaseForm


from .cart_logic import CartLogic



def cart_view(request):

	# TODO: 
	cart_logic = CartLogic(request)

	increase_quantity_form = IncreaseForm()
	decrease_quantity_form = DecreaseForm()

	context = { 
			"cart":cart_logic,
			"increase_form" : increase_quantity_form,
			"decrease_form" : decrease_quantity_form
			
			}


	return render(request, 'cart.html', context)




def add_to_cart_view(request, slug):

	print("Ar trebui adaugat in cos..", slug)
	print("Sesiunea curenta:", request.session)
	
	print("Sesiune", request.POST)



	cart_logic = CartLogic(request)
	quantity = request.POST.get("quantity", 1)
	quantity = int(quantity)

	cart_logic.add(slug, quantity)

	return redirect("cart_url")



def increase_quantity_view(request, slug):
	cart_logic = CartLogic(request)
	cart_logic.increase(slug)
	return redirect("cart_url")


def decrease_quantity_view(request, slug):
	cart_logic = CartLogic(request)
	cart_logic.decrease(slug)
	return redirect("cart_url")


def erase_cart_view(request):
	cart_logic = CartLogic(request)
	cart_logic.clear()

	return redirect("cart_url")