
from django import forms

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