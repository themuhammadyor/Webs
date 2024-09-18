from django.contrib import admin

from .models import User, Notification


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'phone')
    search_fields = ('username', 'email', 'phone')


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
