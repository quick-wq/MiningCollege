from django.contrib import admin
from .models import ConfirmationCode, AuthorizationHistory


@admin.register(ConfirmationCode)
class ConfirmationCodeAdmin(admin.ModelAdmin):
    pass


@admin.register(AuthorizationHistory)
class AuthorizationHistoryAdmin(admin.ModelAdmin):
    pass
