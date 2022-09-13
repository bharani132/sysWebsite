from django.contrib import admin
from .models import employee,year_of_service,project,customer,services,info
# Register your models here.
admin.site.register(employee)
admin.site.register(services)
admin.site.register(customer)
admin.site.register(project)
admin.site.register(year_of_service)
admin.site.register(info)