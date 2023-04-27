from django.urls import path
from .views import (
    LoginView,
    VendorRegisterView,
    CustomerRegisterView,
    VendorListAPIView,
    VendorProfileAPIView,
    VendorDetailAPIView,
    CustomerListAPIView,
)

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('vendor/register/', VendorRegisterView.as_view(), name='vendor-register'),
    path('customer/register/', CustomerRegisterView.as_view(), name='customer-register'),

    path('vendor/list/', VendorListAPIView.as_view(), name='vendor-list'),
    path('customer/list/', CustomerListAPIView.as_view(), name='customer-list'),

    path('vendor/profile/<str:token>/', VendorProfileAPIView.as_view(), name='vendor-profile'),

    path('vendor/detail/<int:id>/', VendorDetailAPIView.as_view(), name='vendor-detail'),
]
