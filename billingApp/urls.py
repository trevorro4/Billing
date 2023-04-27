from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import BillingProfileList, BillingProfileDetail

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/billing-profiles/', BillingProfileList.as_view(),
         name='billing-profile-list'),
    path('api/billing-profiles/<int:pk>/',
         BillingProfileDetail.as_view(), name='billing-profile-detail'),
]
