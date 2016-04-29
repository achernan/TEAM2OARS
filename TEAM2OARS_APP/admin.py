from django.contrib import admin
from .models import Testimonies
from .models import Tenant
from .models import Staff
from .models import Handle_Rents
from .models import Complaints
from .models import Tenant_Family
from .models import Automobiles
from .models import Invoices
from .models import Apartment

# Register your models here.
admin.site.register(Testimonies)
admin.site.register(Tenant)
admin.site.register(Staff)
admin.site.register(Handle_Rents)
admin.site.register(Complaints)
admin.site.register(Tenant_Family)
admin.site.register(Automobiles)
admin.site.register(Invoices)
admin.site.register(Apartment)
