from django.db import models

# Create your models here.
from django.db import models


class BillingProfile(models.Model):
    profileId = models.AutoField(primary_key=True)
    date_created = models.DateTimeField(auto_now_add=True)
    ownerId = models.IntegerField()
    itemId = models.IntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    billingRules = models.ForeignKey('BillingRules', on_delete=models.CASCADE)
    lastModified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'BillingProfile-{self.profileId}'

    class Meta:
        verbose_name = 'Billing Profile'
        verbose_name_plural = 'Billing Profiles'


class Discounts(models.Model):
    discountID = models.AutoField(primary_key=True)
    ownerId = models.IntegerField()
    billingProfile = models.ForeignKey(
        BillingProfile, on_delete=models.CASCADE)
    createdOn = models.DateTimeField(auto_now_add=True)
    validTill = models.DateTimeField()
    status = models.BooleanField()
    eligibility = models.ForeignKey('Eligibility', on_delete=models.CASCADE)

    def __str__(self):
        return f'Discount-{self.discountID }'


class CheckoutMethods(models.Model):
    ID = models.AutoField(primary_key=True)
    methodType = models.CharField(max_length=100)
    createdOn = models.DateTimeField(auto_now_add=True)
    eligibility = models.ForeignKey('Eligibility', on_delete=models.CASCADE)

    def __str__(self):
        return f'CheckoutMethod-{self.ID}'


class PlatformCharges(models.Model):
    chargeId = models.AutoField(primary_key=True)
    billingProfile = models.ForeignKey(
        BillingProfile, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    createdOn = models.DateTimeField(auto_now_add=True)
    createdBy = models.IntegerField()
    eligibility = models.ForeignKey('Eligibility', on_delete=models.CASCADE)

    def __str__(self):
        return f'PlatformCharge-{self.chargeId}'


class Eligibility(models.Model):
    id = models.AutoField(primary_key=True)
    userCategory = models.CharField(max_length=100)
    ruleParameter = models.CharField(max_length=100)
    ruleValue = models.CharField(max_length=100)

    def __str__(self):
        return f'Eligibility-{self.id}'


class Orders(models.Model):
    orderId = models.AutoField(primary_key=True)
    itemId = models.IntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    billingProfile = models.ForeignKey(
        BillingProfile, on_delete=models.CASCADE)
    orderedBy = models.IntegerField()
    orderedOn = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField()

    def __str__(self):
        return f'Order-{self.orderId}'


class Payment(models.Model):
    paymentRef = models.CharField(max_length=100, primary_key=True)
    transactionId = models.CharField(max_length=100)
    checkoutMethod = models.ForeignKey(
        CheckoutMethods, on_delete=models.CASCADE)
    order = models.OneToOneField(Orders, on_delete=models.CASCADE)
    status = models.BooleanField()

    def __str__(self):
        return f'Payment-{self.paymentRef}'


class BillingRules(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'BillingRule-{self.name}'
