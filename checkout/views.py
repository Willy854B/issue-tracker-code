from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MakePaymentForm, OrderForm
from .models import OrderLineItem
from django.conf import settings
from django.utils import timezone
from tickets.models import Ticket
import stripe

# Create your views here.
stripe.api_key = settings.STRIPE_SECRET

@login_required()
def checkout(request):
    if request.method == "POST":
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)

        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.save()
        
            ticket = get_object_or_404(Ticket, pk=id)
        
            order_line_item = OrderLineItem(
                order=order,
                ticket=ticket,
                price=30,
            )
            order_line_item.save()
                    
            try:
                customer = stripe.Charge.create(
                    amount=int(3000),
                    currency="USD",
                    description=request.user.email,
                    card=payment_form.cleaned_data['stripe_id']
                )
            except stripe.error.CardError:
                    messages.error(request, "Your card was declined!")
            
            if customer.paid:
                messages.error(request, "You have successfully paid")
                return redirect(reverse('tickets'))
            else:
                messages.error(request, "Unable to take payment")
        else:
            print(payment_form.errors)
            messages.error(request, "We were unable to take a payment with that card!") 
    else:
        payment_form = MakePaymentForm()
        order_form = OrderForm()
    
    return render(request, "checkout.html", {"order_form": order_form, "payment_form": payment_form, "publishable": settings.STRIPE_PUBLISHABLE})  