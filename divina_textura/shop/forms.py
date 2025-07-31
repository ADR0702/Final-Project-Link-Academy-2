from django import forms
from .models import ProductImage
from django.forms.models import BaseInlineFormSet


class AddToCartForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, max_value=12, initial=1)


class UpdateQuantityForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, max_value=12)


class IncreaseForm(forms.Form):
    pass


class DecreaseForm(forms.Form):
    pass


class EraseCartForm(forms.Form):
    pass





class ProductImageInlineFormSet(BaseInlineFormSet):
    def save_new(self, form, commit=True):
        images = self.files.getlist(form.add_prefix('image'))
        product = form.instance.product if hasattr(form.instance, 'product') else form.instance

        instances = []
        for image in images:
            instance = ProductImage(product=product, image=image)
            if commit:
                instance.save()
            instances.append(instance)
        return instances
