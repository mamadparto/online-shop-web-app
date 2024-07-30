from products.models import Product
from django.contrib import messages


class Cart:
    def __init__(self, request):

        """
        Initialize the cart
        """
        self.request = request

        self.session = request.session

        cart = self.session.get('cart')

        if not cart:
            cart = self.session['cart'] = {}

        self.cart = cart

    def add(self, product, quantity=1, replace_current_quantity=False):

        """
        Add the specified product to the cart if it exists
        """
        product_id = str(product.id)

        if product_id not in self.cart:
            self.cart[product_id] = {'quantity' : 0}
            
        if replace_current_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity

        messages.success(self.request, 'product successfully added to cart')

        self.save()
    def remove(self, product):
        """
        Remove the specified product from the cart if it exists
        """

        product_id = str(product.id)
        
        if product_id in self.cart:
            del self.cart[product_id]

            messages.success(self.request, 'product successfully remove')

            self.save()

    def save(self):

        """
        Mark session as mdified to save changes
        """
        self.session.modified = True

        

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)

        Cart = self.cart.copy()

        for product in products:
            Cart[str(product.id)]['product_obj'] = product
        
        for item in Cart.values():
            item['total_price'] = item['product_obj'].price * item['quantity']
            yield item


    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def clear(self):
        del self.session['cart']
        self.save()

    def get_total_price(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)

        return sum(item['quantity'] * item['product_obj'].price for item in self.cart.values())