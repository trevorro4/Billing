from rest_framework import serializers
from .models import BillingProfile, Discounts
# maps BillingProfile model to a JSON representation.


class BillingProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillingProfile
        fields = '__all__'


class DiscountsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discounts
        fields = ['discountID', 'ownerId', 'billingProfile',
                  'BillingProfile', 'createdOn', 'validTill', 'status', 'eligibility']
