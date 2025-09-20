from django.shortcuts import render, redirect
from shop.models import Product
from shop.forms import IncreaseForm, DecreaseForm
from .cart_logic import CartLogic
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import render_to_string
from django.http import JsonResponse

def cart_view(request):
    cart_logic = CartLogic(request)

    increase_quantity_form = IncreaseForm()
    decrease_quantity_form = DecreaseForm()

    context = {
        "cart": cart_logic,
        "increase_form": increase_quantity_form,
        "decrease_form": decrease_quantity_form
    }
    return render(request, 'cart.html', context)


def add_to_cart_view(request, slug):
    cart_logic = CartLogic(request)
    quantity = int(request.POST.get("quantity", 1))
    size = request.POST.get("size", "N/A")

    cart_logic.add(slug, quantity, size)

    return redirect("cart_url")


def increase_quantity_view(request, key):
    cart_logic = CartLogic(request)
    cart_logic.increase(key)
    return redirect("cart_url")


def decrease_quantity_view(request, key):
    cart_logic = CartLogic(request)
    cart_logic.decrease(key)
    return redirect("cart_url")


def erase_cart_view(request):
    cart_logic = CartLogic(request)
    cart_logic.clear()
    return redirect("cart_url")


def remove_product_view(request, key):
    cart_logic = CartLogic(request)
    cart_logic.remove(key)
    return redirect("cart_url")


def checkout_view(request):
    return render(request, 'checkout.html')


def checkout_process_view(request):
    if request.method == "POST":
        return render(request, 'checkout_success.html')

    return redirect('checkout_url')


# ------------------ Hover Cart View ------------------

def cart_hover_view(request):
    cart_logic = CartLogic(request)

    html = render_to_string('cart_hover_content.html', {'cart': cart_logic})

    return JsonResponse({'html': html})

def cart_item_count_view(request):
    cart_logic = CartLogic(request)
    item_count = sum(item['quantity'] for item in cart_logic.items.values())
    return JsonResponse({'item_count': item_count})