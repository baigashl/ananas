from django.urls import path
from .views import (
    ProductListAPIView,
    ProductCreateAPIView,
    ProductDetailAPIView,
    ProductUpdateAPIView,
    ProductDeleteAPIView,
    CartDetailAPIView,
    AddToCartAPIView,
)

urlpatterns = [
    path('list/', ProductListAPIView.as_view(), name='product-list'),
    path('create/', ProductCreateAPIView.as_view(), name='product-create'),
    path('<int:id>/', ProductDetailAPIView.as_view(), name='product-detail'),
    path('<int:id>/update/', ProductUpdateAPIView.as_view(), name='product-update'),
    path('<int:id>/delete/', ProductDeleteAPIView.as_view(), name='product-delete'),

    path('cart/<int:user_id>/', CartDetailAPIView.as_view(), name='cart'),
    path('cart/<int:user_id>/add/', AddToCartAPIView.as_view(), name='add-cart'),
]

