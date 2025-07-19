from django.core.management.base import BaseCommand, CommandError
from shop.models import Category
import requests

### python manage.py fetch_categories
class Command(BaseCommand):
    help = "Fetch categories from https://dummyjson.com/products/categories"

    def handle(self, *args, **options):
        BASE_URL = "https://dummyjson.com/"
        URL_CATEGORIES = BASE_URL + "products/categories"
        response = requests.get(URL_CATEGORIES)
        categories_list = response.json()
        for cat_dict in categories_list:
            Category.objects.create(name=cat_dict["name"], slug=cat_dict["slug"])
            print("A fost creata categoria:", cat_dict["name"])
        print("S-a terminat...")
