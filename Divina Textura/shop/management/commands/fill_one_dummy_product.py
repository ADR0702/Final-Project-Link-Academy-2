from django.core.management.base import BaseCommand, CommandError
from shop.models import Product
import random

### python manage.py fill_one_dummy_product
class Command(BaseCommand):
    help = "Create a dummy product with random name"

    def handle(self, *args, **options):
        random_no = random.randint(1, 100)
        try:
            new_product = Product(name=f"Produsul {random_no}", price=random_no, slug=f"produsul-{random_no}")
            new_product.save()
            self.stdout.write(
                    self.style.SUCCESS("Successfully created a new product")
                )
        except:
            self.stdout.write(
                    self.style.ERROR("Could not create that product")
                )