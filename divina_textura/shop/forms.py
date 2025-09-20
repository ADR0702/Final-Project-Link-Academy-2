from django import forms
from .models import ProductImage
from django.forms.models import BaseInlineFormSet
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


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
        # Obține imaginea trimisă (una singură) — Django admin nu suportă multiple implicit
        image = form.cleaned_data.get('image')
        if image:
            instance = form.save(commit=False)
            instance.image = image
            if commit:
                instance.save()
            return instance
        return None


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your email address'
        })
    )

    class Meta:
        model = CustomUser
        fields = ("email", "password1", "password2")