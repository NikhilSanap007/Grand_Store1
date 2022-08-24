from django.contrib import admin
from .models import parts, Contact

# Register your models here.

admin.site.register(parts)
admin.site.register(Contact)