from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import ImageField, ForeignKey, CASCADE, CharField, TextField, TimeField
from phone_field import PhoneField
from django.utils import timezone

from apps.shared.models import AbstractBaseModel


class User(AbstractUser, AbstractBaseModel):
    phone = PhoneField(blank=True, help_text='Contact phone number')
    avatar = ImageField(upload_to='users/avatars/covers/')

    def __str__(self):
        return self.username


class Notification(AbstractBaseModel):
    sender_user = ForeignKey(User, on_delete=CASCADE, related_name='send_notifications')
    receive_user = ForeignKey(User, on_delete=CASCADE, related_name='receive_notifications')
    title = CharField(max_length=255)
    content = TextField()
    send_time = TimeField(default=timezone.now)

    def __str__(self):
        return self.title
