from django.shortcuts import render

from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .models import BillingProfile, Discounts, CheckoutMethods, PlatformCharges, Eligibility, Orders, Payment, BillingRules
from .serializers import BillingProfileSerializer
from django.http import HttpResponse

# single responsibility app


def create_billing_profile(request):
    if request.method == 'POST':
        owner_id = request.POST.get('owner_id')
        item_id = request.POST.get('item_id')
        amount = request.POST.get('amount')

        # Validate input
        if not owner_id or not item_id or not amount:
            return HttpResponse("Invalid input")

        # Create a new billing profile
        billing_profile = BillingProfile.objects.create(
            ownerId=owner_id,
            itemId=item_id,
            amount=amount,
        )

        return HttpResponse("Billing profile created successfully")


def create_discount(request):
    if request.method == 'POST':
        owner_id = request.POST.get('owner_id')
        billing_profile_id = request.POST.get('billing_profile_id')
        valid_till = request.POST.get('valid_till')
        eligibility_id = request.POST.get('eligibility_id')

        # Validate input
        if not owner_id or not billing_profile_id or not valid_till or not eligibility_id:
            return HttpResponse("Invalid input")

        # Create a new discount
        discount = Discounts.objects.create(
            ownerId=owner_id,
            billingProfile_id=billing_profile_id,
            validTill=valid_till,
            eligibility_id=eligibility_id,
            status=True
        )

        return HttpResponse("Discount created successfully")


def create_checkout_method(request):
    if request.method == 'POST':
        method_type = request.POST.get('method_type')
        eligibility_id = request.POST.get('eligibility_id')

        # Validate input
        if not method_type or not eligibility_id:
            return HttpResponse("Invalid input")

        # Create a new checkout method
        checkout_method = CheckoutMethods.objects.create(
            methodType=method_type,
            eligibility_id=eligibility_id
        )

        return HttpResponse("Checkout method created successfully")


def create_platform_charge(request):
    if request.method == 'POST':
        billing_profile_id = request.POST.get('billing_profile_id')
        amount = request.POST.get('amount')
        created_by = request.POST.get('created_by')
        eligibility_id = request.POST.get('eligibility_id')

        # Validate input
        if not billing_profile_id or not amount or not created_by or not eligibility_id:
            return HttpResponse("Invalid input")

        # Create a new platform charge
        platform_charge = PlatformCharges.objects.create(
            billingProfile_id=billing_profile_id,
            amount=amount,
            createdBy=created_by,
            eligibility_id=eligibility_id
        )

        return HttpResponse("Platform charge created successfully")


def create_eligibility(request):
    if request.method == 'POST':
        user_category = request.POST.get('user_category')
        rule_parameter = request.POST.get('rule_parameter')
        rule_value = request.POST.get('rule_value')

        # Validate input
        if not user_category or not rule_parameter or not rule_value:
            return HttpResponse("Invalid input")

        # Create a new eligibility
        eligibility = Eligibility.objects.create(
            userCategory=user_category,
            ruleParameter=rule_parameter,
            ruleValue=rule_value
        )

        return HttpResponse("Eligibility created successfully")


def create_order(request):
    if request.method == 'POST':
        item_id = request.POST.get('item_id')
        amount = request.POST.get('amount')
        billing_profile_id = request.POST.get('billing_profile_id')
        ordered_by = request.POST.get('ordered_by')

        # Validate input
        if not item_id or not amount or not billing_profile_id or not ordered_by:
            return HttpResponse("Invalid input")

        # Create a new order
        order = Orders.objects.create(
            itemId=item_id,
            amount=amount,
            billingProfile_id=billing_profile_id,
            orderedBy=ordered_by,
            status=True
        )

        return HttpResponse("Order created successfully")


def create_payment(request):
    if request.method == 'POST':
        payment_ref = request.POST.get('payment_ref')
        transaction_id = request.POST.get('transaction_id')
        checkout_method_id = request.POST.get('checkout_method_id')
        order_id = request.POST.get('order_id')

        # Validate input
        if not payment_ref or not transaction_id or not checkout_method_id or not order_id:
            return HttpResponse("Invalid input")

        # Create a new payment
        payment = Payment.objects.create(
            paymentRef=payment_ref,
            transactionId=transaction_id,
            checkoutMethod_id=checkout_method_id,
            order_id=order_id,
            status=True
        )

        return HttpResponse("Payment created successfully")


def create_billing_rule(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        if name and description:
            BillingRules.objects.create(name=name, description=description)
            return HttpResponse("Billing rule created successfully")
        else:
            return HttpResponse("Invalid input")
    # render a template with a form to create a new billing rule
    return render(request, 'create_billing_rule.html')


# API endpoints with serializers
class BillingProfileList(generics.ListCreateAPIView):
    queryset = BillingProfile.objects.all()
    serializer_class = BillingProfileSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(ownerId=self.request.user.id)


class BillingProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BillingProfile.objects.all()
    serializer_class = BillingProfileSerializer
    permission_classes = (permissions.IsAuthenticated,)
