from rest_framework import serializers
from .models import BillingProfile
# maps BillingProfile model to a JSON representation.


class BillingProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillingProfile
        fields = '__all__'
