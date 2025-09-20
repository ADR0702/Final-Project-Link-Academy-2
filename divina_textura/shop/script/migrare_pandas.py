import pandas as pd
from shop.models import Category, Subcategories, Product

def migreaza_produse_cu_pandas(cale_csv_produse, cale_csv_categorii, cale_csv_subcategorii):
    # Citește CSV-urile exportate din baza veche
    df_categorii = pd.read_csv(cale_csv_categorii)
    df_subcategorii = pd.read_csv(cale_csv_subcategorii)
    df_produse = pd.read_csv(cale_csv_produse)
    
    # Migrează categoriile
    categorii_map = {}
    for _, row in df_categorii.iterrows():
        cat, _ = Category.objects.get_or_create(name=row['name'], slug=row['slug'])
        categorii_map[row['id']] = cat

    # Migrează subcategoriile
    subcategorii_map = {}
    for _, row in df_subcategorii.iterrows():
        parent_cat = categorii_map.get(row['parent_category_id'])
        subcat, _ = Subcategories.objects.get_or_create(name=row['name'], slug=row['slug'], parent_category=parent_cat)
        subcategorii_map[row['id']] = subcat

    # Migrează produsele
    for _, row in df_produse.iterrows():
        produs = Product.objects.create(
            name=row['name'],
            slug=row['slug'],
            description=row['description'],
            price=row['price'],
            # image trebuie tratată separat, vezi mai jos
        )
        # Leagă categoriile (multe la multe)
        cat_ids = [int(x) for x in row['category_ids'].split(',')]  # presupunem că ai un câmp cu ID-uri separate prin virgulă
        for cat_id in cat_ids:
            cat = categorii_map.get(cat_id)
            if cat:
                produs.categories.add(cat)
        
        # Leagă subcategoria dacă există
        subcat_id = row.get('subcategory_id')
        if pd.notnull(subcat_id):
            subcat = subcategorii_map.get(int(subcat_id))
            if subcat:
                produs.subcategory = subcat
                produs.save()
        
        # Imaginea trebuie copiată separat în media folder și linkată corect în db

    print("Migrarea s-a finalizat cu succes!")
