from django import forms

from . models import Order

class OrderForms(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["first_name", "last_name", "phon_number", "address", "order_nots"]
        # widgets = {
        #     'order_nots' : forms.Textarea(attrs={'rows': 5, 'placeholder': 'write your nots here.'}),
        #     'address' : forms.Textarea(attrs={'rows': 3}),

        # }