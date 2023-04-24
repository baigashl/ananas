from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer


class ProductListAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        all_product = Product.objects.all()
        serializer = ProductSerializer(all_product, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductCreateAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            product = Product.objects.create(
                vendor_id=request.data['vendor'],
                category_id=request.data['category'],
                name=request.data['name'],
                description=request.data['description'],
                price=request.data['price']
            )
            product.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


