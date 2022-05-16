from django.contrib import admin
from .models.staffs import Staffs
from .models.departments import Departments
from .models.staff_types import StaffTypes
from .models.users import Users
from .models.inspections import Inspections
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    list_display = (
        'username', 'email', 'is_staff', 'staff'
    )
    fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        ('Доп. инфо', {
            'fields': ('staff',)
        }),
        ('Права', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions'
            )
        }),
        ('Даты', {
            'fields': ('last_login', 'date_joined')
        }),

    )


# Register your models here.
admin.site.register(Staffs)
admin.site.register(Departments)
admin.site.register(StaffTypes)
admin.site.register(Users, CustomUserAdmin)
admin.site.register(Inspections)
