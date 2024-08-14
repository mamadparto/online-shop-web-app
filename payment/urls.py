from django.urls import path


from  . import views

app_name='payment'

urlpatterns = [
    path('proccess/', views.payment_proccess, name='payment_proccess'),
]