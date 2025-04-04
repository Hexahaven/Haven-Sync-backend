from django.contrib import admin

# Register your models here.

from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'full_name', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    search_fields = ('email', 'full_name')
    ordering = ('-id',)
    list_per_page = 20
    list_display_links = ('id', 'email')
    fieldsets = (
        (None, {'fields': ('email', 'full_name', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {'fields': ('email', 'full_name', 'password1', 'password2')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )

admin.site.register(User, UserAdmin)
admin.site.site_header = "Hexa Haven Admin"