from django.contrib import admin

from .models import Member, Message, SheduledMessage

admin.site.register(Member)
admin.site.register(Message)
admin.site.register(SheduledMessage)