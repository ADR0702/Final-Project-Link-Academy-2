from shop.models import Product


class CartLogic:
    def __init__(self, request):
        self.request = request
        # Structura cosului: { "slug_size": {"quantity": X, "size": size} }
        self.produse_existente = request.session.get("cos", {})

    ### Totalul cartului
    @property
    def total_price(self):
        total = 0
        for key, info in self.produse_existente.items():
            slug = key.rsplit('_', 1)[0]  # extragem slugul din cheia "slug_size"
            product = Product.objects.filter(slug=slug).first()
            if product:
                total += product.price * info["quantity"]
        return total

    @property
    def number_of_products(self):
        return sum(info["quantity"] for info in self.produse_existente.values())

    ### Produsele din cart si numarul lor (cu marimi)
    @property
    def products(self):
        # Returnează dict cu {product_obj: {"quantity": X, "size": Y, "total_price": Z}}
        products_dict = {}
        for key, info in self.produse_existente.items():
            slug = key.rsplit('_', 1)[0]
            product = Product.objects.filter(slug=slug).first()
            if product:
                total_price = product.price * info["quantity"]
                products_dict[product] = {
                    "quantity": info["quantity"],
                    "size": info["size"],
                    "total_price": total_price
                }
        return products_dict

    ### Adaugare produs in cart cu marime
    def add(self, slug, quantity, size="N/A"):
        key = f"{slug}_{size}"

        existing = self.produse_existente.get(key, {"quantity": 0, "size": size})
        new_quantity = existing["quantity"] + quantity

        if new_quantity <= 0:
            self.produse_existente.pop(key, None)
        else:
            self.produse_existente[key] = {"quantity": new_quantity, "size": size}

        self.request.session["cos"] = self.produse_existente

    def increase(self, key):
        # key = "slug_size"
        if key in self.produse_existente:
            self.produse_existente[key]["quantity"] += 1
            self.request.session["cos"] = self.produse_existente

    def decrease(self, key):
        # key = "slug_size"
        if key in self.produse_existente:
            self.produse_existente[key]["quantity"] -= 1
            if self.produse_existente[key]["quantity"] <= 0:
                self.produse_existente.pop(key)
            self.request.session["cos"] = self.produse_existente

    ### Stergere produs din cart
    def remove(self, key):
        if key in self.produse_existente:
            self.produse_existente.pop(key)
            self.request.session["cos"] = self.produse_existente

    ### Stergere cart
    def clear(self):
        self.produse_existente = {}
        self.request.session["cos"] = {}
