from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import Vendor, Customer
from .permissions import AnonPermissionOnly
from .serializers import MyTokenObtainPairSerializer, VendorRegisterSerializer, CustomerRegisterSerializer


class LoginView(TokenObtainPairView):
    permission_classes = (AnonPermissionOnly,)
    serializer_class = MyTokenObtainPairSerializer


class VendorRegisterView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = VendorRegisterSerializer(data=request.data)
        if serializer.is_valid():
            vendor = Vendor.objects.create(
                email=request.data['email'],
                name=request.data['name'],
                second_name=request.data['second_name'],
                phone_number=request.data['phone_number'],
                description=request.data['description'],
                is_Vendor=True
            )
            vendor.set_password(request.data['password'])
            vendor.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomerRegisterView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = CustomerRegisterSerializer(data=request.data)
        if serializer.is_valid():
            vendor = Customer.objects.create(
                email=request.data['email'],
                name=request.data['name'],
                second_name=request.data['second_name'],
                phone_number=request.data['phone_number'],
                card_number=request.data['card_number'],
                address=request.data['address'],
                post_code=request.data['post_code'],
                is_Vendor=False
            )
            vendor.set_password(request.data['password'])
            vendor.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VendorListAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        vendors = Vendor.objects.all()
        serializer = VendorRegisterSerializer(vendors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

