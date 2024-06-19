from django.contrib import admin

# Register your models here.
from .models import Role,Employee,Department

admin.site.register(Employee)

admin.site.register(Role)

admin.site.register(Department)