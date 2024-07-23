from django.urls import path

# from .views import ProductListView, ProductDetailView, CommentCreatedView, comment_validation
from . import views

urlpatterns = [
    path('',views.ProductListView.as_view(), name='product_list'),
    path('<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('comment/<int:pk>/', views.CommentCreatedView.as_view(), name='comment_create'),
    # path('comment/validation', views.comment_validation, name='comment_validation')
]