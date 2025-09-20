from django.db import connections
from shop.models import Product, Category, Subcategories

def migreaza_produse_complet():
    with connections['old_db'].cursor() as cursor:
        # Preluam toate produsele cu campurile necesare
        cursor.execute("""
            SELECT id, name, description, slug, price, image, subcategory_id 
            FROM shop_product
        """)
        produse = cursor.fetchall()

        # Import categorii - creăm un dicționar pentru mapare ID vechi -> categorie nouă
        cursor.execute("SELECT id, name, slug FROM shop_category")
        categorii_vechi = cursor.fetchall()
        categorii_map = {}
        for cat_id, name, slug in categorii_vechi:
            cat, _ = Category.objects.get_or_create(name=name, slug=slug)
            categorii_map[cat_id] = cat

        # Import subcategorii
        cursor.execute("SELECT id, name, slug, parent_category_id FROM shop_subcategories")
        subcategorii_vechi = cursor.fetchall()
        subcategorii_map = {}
        for sub_id, name, slug, parent_cat_id in subcategorii_vechi:
            parent_cat = categorii_map.get(parent_cat_id)
            if parent_cat:
                subcat, _ = Subcategories.objects.get_or_create(
                    name=name, slug=slug, parent_category=parent_cat
                )
                subcategorii_map[sub_id] = subcat

        for prod in produse:
            prod_id, name, description, slug, price, image, subcat_id = prod

            # Crează produsul fără categorii mai întâi
            p = Product.objects.create(
                name=name,
                description=description,
                slug=slug,
                price=price,
                image=image,
                subcategory=subcategorii_map.get(subcat_id)
            )

            # Acum trebuie să luăm categoriile ManyToMany din tabelă intermediară:
            cursor.execute("""
                SELECT category_id FROM shop_product_categories WHERE product_id=%s
            """, [prod_id])
            cat_ids = cursor.fetchall()

            for (cat_id,) in cat_ids:
                cat = categorii_map.get(cat_id)
                if cat:
                    p.categories.add(cat)

    print(f"{len(produse)} produse migrate cu categorii și subcategorii.")
