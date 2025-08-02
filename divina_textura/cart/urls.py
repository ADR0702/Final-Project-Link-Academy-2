from django.urls import path
from .views import (
    cart_view,
    add_to_cart_view,
    erase_cart_view,
    increase_quantity_view,
    decrease_quantity_view,
    remove_product_view,
    checkout_view,
    checkout_process_view,
    cart_hover_view,
    cart_item_count_view
)

urlpatterns = [
    path("", cart_view, name="cart_url"),
    path("add/<slug>", add_to_cart_view, name="add_to_cart_url"),
    path("increase/<key>", increase_quantity_view, name="increase_url"),
    path("decrease/<key>", decrease_quantity_view, name="decrease_url"),
    path("remove/<key>", remove_product_view, name="remove_url"),
    path("clear/", erase_cart_view, name="clear_cart_url"),
    path('checkout/', checkout_view, name='checkout_url'),
    path('checkout/process/', checkout_process_view, name='checkout_process_url'),
    path('cart-hover/', cart_hover_view, name='cart_hover_url'),
    path('cart-item-count/', cart_item_count_view, name='cart_item_count_url'),


]
