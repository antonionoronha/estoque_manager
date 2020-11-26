from django import forms
from .models import Product, Purchase


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('name',)
        labels = {
            'name': 'Nome'
        }


class PurchaseForm(forms.ModelForm):

    class Meta:
        model = Purchase
        fields = '__all__'
        labels = {
            'product': 'Produto',
            'amount': 'Quantidade',
            'price': 'Preço de compra',
        }

    def __init__(self, *args, **kwargs):
        super(PurchaseForm, self).__init__(*args, **kwargs)
        self.fields['product'].empty_label = "Selecione o produto..."
