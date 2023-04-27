from django.contrib import admin
from .models import BillingProfile, Discounts, CheckoutMethods, PlatformCharges, Eligibility, Orders, Payment, BillingRules

# Register your models here
admin.site.register(BillingProfile)
admin.site.register(Discounts)
admin.site.register(CheckoutMethods)
admin.site.register(PlatformCharges)
admin.site.register(Eligibility)
admin.site.register(Orders)
admin.site.register(Payment)
admin.site.register(BillingRules)
