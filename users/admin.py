from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import User

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('email','first_name','last_name','is_active')
    list_filter = ('is_staff', 'is_active')
    fieldsets = (
        (None, {
            "fields": (
                'email',
                'password'
            ),
        }),
        ('Personal Informations',{
            "fields": (
                'first_name',
                'last_name',
                'address',
                'phone_number'
            ),
        }),
        ('Permissions',{
            "fields": (
                'is_active',
                'is_staff',
                'is_superuser',
                'user_permissions',
                'groups'
            ),
        }),
        ('Important Date',{
            "fields": (
                'last_login',
                'date_joined'
            ),
        })
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')
        }),
    )
    ordering = ('email',)
    search_fields = ('email', 'first_name', 'last_name')

admin.site.register(User, CustomUserAdmin)