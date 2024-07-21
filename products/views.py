from typing import Any
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import generic
import time

# from .models import Product, ProductComment
from . import models
from .forms import CommentForms

class ProductListView(generic.ListView):
    # model = Product
    queryset = models.Product.objects.filter(active=True)
    template_name = "products/product_list.html"
    context_object_name = 'products'


class ProductDetailView(generic.DetailView):
    queryset = models.Product.objects.filter(active=True)
    # model = Product
    template_name = "products/product_detail.html"
    context_object_name = 'product'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForms()
        return context
    


def comment_validation(request):
    
    time.sleep(5)

    return render(request, "products/comment_validation.html")



class CommentCreatedView(generic.CreateView):
    model = models.ProductComment.objects.filter(active=True)
    form_class = CommentForms



    # def get_success_url(self) -> str:
    #     return render(template_name="products/comment_validation.html")
    


    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user



        Product = get_object_or_404( models.Product, id = int(self.kwargs['pk']))
        obj.product = Product

        return super().form_valid(form)