
from .cart_logic import CartLogic

def add_cart_to_context(request):
    cart = CartLogic(request)
    added_context = {
        "cart" : cart
    }
    return added_context