from rest_framework.serializers import ModelSerializer

from apps.mysite.models import Order
from apps.users.models import User, Notification


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class NotificationSerializer(ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
