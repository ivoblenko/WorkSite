from django.contrib import admin
from .models.staffs import Staffs
from .models.departments import Departments
from .models.staff_types import StaffTypes
from .models.users import Users
from .models.inspections import Inspections

# Register your models here.
admin.site.register(Staffs)
admin.site.register(Departments)
admin.site.register(StaffTypes)
admin.site.register(Users)
admin.site.register(Inspections)