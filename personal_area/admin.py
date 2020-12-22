from django.contrib import admin

from .models import UserPosition, Role, Direction, Group, Event, UserProfile, Participation


@admin.register(UserPosition)
class UserPositionAdmin(admin.ModelAdmin):
    pass


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    pass


@admin.register(Direction)
class DirectionsAdmin(admin.ModelAdmin):
    pass


@admin.register(Group)
class GroupsAdmin(admin.ModelAdmin):
    pass


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    pass


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'position', 'age', 'group', 'genre')
    list_display_links = ('id', 'full_name')
    list_filter = ('position', 'genre')
    readonly_fields = ('user',)


@admin.register(Participation)
class ParticipationAdmin(admin.ModelAdmin):
    pass
