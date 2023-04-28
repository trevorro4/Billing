from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('billing/', include('billingApp.urls')),
    path('admin/', admin.site.urls),
]
