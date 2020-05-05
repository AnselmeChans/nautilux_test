from django.contrib import admin

#from apps.intevrentions.models import Command
from apps.interventions.models import Intervention

class CommandAdmin(admin.ModelAdmin):
    pass


admin.site.register(Intervention, CommandAdmin)
