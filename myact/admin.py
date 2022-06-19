from django.contrib import admin
from myact.models import Activities

from myact.views import insertActs

# Register your models here.
admin.site.register(Activities)