from django import forms

from .models import ProductComment


class CommentForms(forms.ModelForm):
    class Meta:
        model = ProductComment
        fields = ['body', 'stars',]
