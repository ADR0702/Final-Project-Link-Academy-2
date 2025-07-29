from django.urls import path
from .views import (
    home_view,
    product_details_view,
    all_categories_view,
    category_details_view,
    subcategory_details_view,
)

urlpatterns = [
    path("", home_view, name="home_url"),
    path("details", product_details_view),

    # Pagina cu cele 3 categorii (Women, Men, Kids)
    path("categories", all_categories_view, name="categories_url"),

    # Detaliile pentru fiecare categorie
    path("categories/<slug:slug>/", category_details_view, name="category_detail_url"),

    path("product/<slug:slug>/", product_details_view, name="product_detail_url"),

    path("categorii/<slug:parent_slug>/<slug:sub_slug>/", subcategory_details_view, name="subcategory_detail_url"),

]
