from django.urls import path
from .views import LoginView, VendorRegisterView, CustomerRegisterView, VendorListAPIView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('vendor/register/', VendorRegisterView.as_view(), name='vendor-register'),
    path('customer/register/', CustomerRegisterView.as_view(), name='customer-register'),

    path('vendor/list/', VendorListAPIView.as_view(), name='vendor-list'),
]
