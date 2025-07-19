from django.urls import path
from .views import category_details_view
from .views import all_categories_view
from .views import product_details_view
from .views import home_view


urlpatterns = [

	path("", home_view, name="home_url"),
	path("details", product_details_view),
	path("categories", all_categories_view, name="categories_url"),
	path("categories/<slug>", category_details_view),
    
	

]
