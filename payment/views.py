from django.shortcuts import render, redirect
from cart.cart import Cart
from payment.forms import ShippingForm, PaymentForm
from payment.models import ShippingAddress
from django.contrib import messages

def process_order(request):
    if request.POST:
        # Get Billing Info from the last page
        payment_form = PaymentForm(request.POST or None)
        # Get Shipping Session Data
        my_shipping = request.session.get('my_shipping')
        print(my_shipping)
        messages.success(request, "Order Placed!")
        return redirect('home')
    else:
        messages.success(request, "Access Denied - Acesso Negado")
        return redirect('home')


def billing_info(request):
    if request.POST:
        # get the cart
        cart = Cart(request)
        cart_products = cart.get_prods
        quantities = cart.get_quants
        totals = cart.cart_total()

        # Create a Session with Shipping Info
        my_shipping = request.POST
        request.session['my_shipping'] = my_shipping
        # Check to see if user is logged in
        if request.user.is_authenticated:
            # Get the Billing Form
            billing_form = PaymentForm()
            return render(request, "payment/billing_info.html", {"cart_products":cart_products, "quantities":quantities, "totals":totals, "shipping_info":request.POST, "billing_form":billing_form }) 
        else:
            # Not logged in
            # Get the Billing Form
            billing_form = PaymentForm()
            return render(request, "payment/billing_info.html", {"cart_products":cart_products, "quantities":quantities, "totals":totals, "shipping_form":request.POST, "billing_form":billing_form })  

#        shipping_form = ShippingForm(request.POST or None)
#        return render(request, "payment/billing_info.html", {"cart_products":cart_products, "quantities":quantities, "totals":totals, "shipping_form":shipping_form})   
    else:
        messages.success(request, "Access Denied - Acesso Negado")
        return redirect('home')

 
def checkout(request):
    # Get the cart
    cart = Cart(request)
    cart_products = cart.get_prods
    quantities = cart.get_quants
    totals = cart.cart_total()

    if request.user.is_authenticated:
        # Checkout as logged in user
        # Get User's Shipping User
        shipping_user = ShippingAddress.objects.get(user__id=request.user.id)
        # Get User's Shipping Form
        shipping_form = ShippingForm(request.POST or None, instance=shipping_user)

        return render(request, "payment/checkout.html", {"cart_products":cart_products, "quantities":quantities, "totals":totals, "shipping_form":shipping_form })
    else:
        # Checkout as guest
        shipping_form = ShippingForm(request.POST or None)
        return render(request, "payment/checkout.html", {"cart_products":cart_products, "quantities":quantities, "totals":totals, "shipping_form":shipping_form })


def payment_success(request):
    return render(request, "payment/payment_success.html", {})

