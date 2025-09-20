from .models import Cart
def cart_processor(request):
    cart = None
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user, is_active=True).first()
    else:
        # ex: preia coșul din sesiune
        session_cart = request.session.get('cart', {})
        # aici creează un obiect custom cu items ca listă
        class SessionCart:
            def __init__(self, items):
                self.items = items
            def items_exists(self):
                return bool(self.items)
            def items_count(self):
                return sum(item['quantity'] for item in self.items)
        items = []
        for product_id, data in session_cart.items():
            # în realitate, aici ai încărca produsul din DB
            items.append({'product': {'name': f"Produs {product_id}"}, 'quantity': data['quantity']})
        cart = SessionCart(items)
    return {'cart': cart}
