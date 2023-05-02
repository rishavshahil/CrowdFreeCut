from django.contrib import admin
from .models import BookingRequest, CustomerNotification

@admin.register(BookingRequest)
class BookingRequestModelAdmin(admin.ModelAdmin):
    list_display = ['salon', 'customer']
    
@admin.register(CustomerNotification)
class CustomerNotificationModelAdmin(admin.ModelAdmin):
    list_display = []