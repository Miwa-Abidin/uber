from django.shortcuts import render
from .models import Taxi, Order, StatusDriver, StatusType
from rest_framework import generics, viewsets
from .serializers import TaxiSerializer, OrderSerializer, StatusDriverSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.response import Response
from .permissions import IsDriverPermission, IsClientPermission

class TaxiViewSet(viewsets.ModelViewSet):
    queryset = Taxi.objects.all()
    serializer_class = TaxiSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, ]

    def perform_create(self, serializer):
        serializer.save(profile=self.request.user.profile)



    # @action(methods=['POST'], detail=True)
    # def leave_status(self, request, pk=None):
    #     serializer = StatusDriverSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save(
    #             taxi=self.get_object(),
    #             profile=request.user.profile
    #         )
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     else:
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaxiCreateRetrieveDestroyApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Taxi.objects.all()
    serializer_class = TaxiSerializer
    permission_classes = [IsDriverPermission, ]


class OrderViewSet(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, ]


    def perform_create(self, serializer):
        serializer.save(profile=self.request.user.profile)


class OrderRetrieveUpdateDestroyApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsClientPermission, ]





