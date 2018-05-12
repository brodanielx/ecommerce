from django.shortcuts import render

import stripe
stripe.api_key = 'sk_test_xhUCOpSvefHALlsGQufxUfm3'
STRIPE_PUB_KEY = 'pk_test_HtxVLz47gz3gHg5Y6oD2e0p3'


def payment_method_view(request):
    if request.method == 'POST':
        print(request.POST)
    return render(request, 'billing/payment-method.html', {'publish_key': STRIPE_PUB_KEY})
