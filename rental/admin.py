from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Role, User, Car, ContactDetail

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'role', 'is_staff', 'is_active')
    list_filter = ('role', 'is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('email', 'phone', 'profile_picture')}),
        ('Role', {'fields': ('role',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'role', 'phone'),
        }),
    )
    search_fields = ('username', 'email', 'phone')
    ordering = ('username',)

# Register your models here.
admin.site.register(Role)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Car)
admin.site.register(ContactDetail)
