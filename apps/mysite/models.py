from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import CharField, TextField, ForeignKey, CASCADE, TimeField, DateField, DecimalField, \
    BooleanField, PositiveIntegerField
from django.utils import timezone

from apps.shared.models import AbstractBaseModel


class Order(AbstractBaseModel):
    title = CharField(max_length=255)
    content = TextField()
    technology = TextField()
    experience = PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    user = ForeignKey('users.User', on_delete=CASCADE, related_name='orders')
    time = TimeField(default=timezone.now)
    price = DecimalField(max_digits=10, decimal_places=2, null=True)
    start_date = DateField()
    end_date = DateField()
    is_active = BooleanField(default=False)
    is_accepted = BooleanField(default=False)

    def __str__(self):
        return self.title
