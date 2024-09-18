from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import *


class UserAPIViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class NotificationAPIViewSet(ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer


class OrderAPIViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
