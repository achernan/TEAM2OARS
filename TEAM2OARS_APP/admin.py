from django.contrib import admin
from .models import Testimonies
from .models import Tenant
from .models import Staff

# Register your models here.
admin.site.register(Testimonies)
admin.site.register(Tenant)
admin.site.register(Staff)
