from django.contrib import admin
from mapbox_location_field.admin import MapAdmin

from .models import (
    EventCategory,
    Event,
    JobCategory,
    EventJobCategoryLinking,
    EventMember,
    UserProfile,
)


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone_number', 'created_date']
    list_filter = ['created_date']
    search_fields = ['user__username', 'user__first_name', 'user__last_name', 'phone_number']


@admin.register(EventCategory)
class EventCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'status', 'created_date']
    list_filter = ['status', 'created_date']
    search_fields = ['name', 'code']
    exclude = ['priority']


@admin.register(Event)
class EventAdmin(MapAdmin):
    list_display = ['name', 'category', 'venue', 'start_date', 'end_date', 'status']
    list_filter = ['status', 'category', 'start_date']
    search_fields = ['name', 'venue']
    exclude = ['location']


admin.site.register(JobCategory)
admin.site.register(EventJobCategoryLinking)
admin.site.register(EventMember)
