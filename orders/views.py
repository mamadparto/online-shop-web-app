from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib import messages

from .forms import OrderForms
from cart.cart import Cart
from .models import OrderItem

@login_required
def order_created_view(request):
    order_form = OrderForms()
    cart = Cart(request)

    if len(cart) == 0:
        messages.warning(request, 'you can proceed to checkout page because your cart is empty.')
        return redirect('product_list')

    if request.method == 'POST':
        order_form = OrderForms(request.POST,)

        
        

        if order_form.is_valid():
            order_obj = order_form.save(commit=False)
            order_obj.user = request.user
            order_obj.save()


            for item in cart:
                product = item['product_obj']
                OrderItem.objects.create(
                    order = order_obj,
                    product = product,
                    quantity = item['quantity'],
                    price = product.price,
                )

            cart.clear()

            request.user.first_name = order_obj.first_name
            request.user.last_name = order_obj.last_name
            request.user.save()

            request.session['order_id'] = order_obj.id
            return redirect('payment:payment_proccess')




    return render(request, 'orders/order_created.html',{
        'form': order_form,
    })