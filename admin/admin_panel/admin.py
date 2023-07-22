from django.contrib import admin
from .models import (System, Service, SystemAlias, SystemService,
                     SystemServiceMainTeams, SystemServiceСompetenceTeams,
                     SystemServicePyrusForms, PyrusForms)

# Register your models here.


@admin.register(System)
class SystemAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', )

    list_filter = ('name', )

    search_fields = ('name', 'description', )

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', )

    list_filter = ('name', )

    search_fields = ('name', 'description', )

@admin.register(SystemAlias)
class SystemAliasAdmin(admin.ModelAdmin):
    list_display = ('alias', )
    search_fields = ('alias', )


@admin.register(SystemService)
class SystemServiceAdmin(admin.ModelAdmin):
    list_display = ('system', 'service', 'plan_time', 'start_support_time',
                    'end_support_time', )
    # fieldsets=(        
    #    ("My Group",{
    #        "fields": (tuple(['system','service']),
    #                   ),
    #                   }), 
    # )
    list_filter = ('system', 'service', )
    filter_horizontal = ('system_service_main_teams', 'system_service_competence_teams', )

@admin.register(SystemServiceMainTeams)
class SystemServiceMainTeamsAdmin(admin.ModelAdmin):
    list_display = ('role_id', 'role_name', 'plan_time', 'pyrus_stage', )


@admin.register(SystemServiceСompetenceTeams)
class SystemServiceСompetenceTeamsAdmin(admin.ModelAdmin):
    list_display = ('role_id', 'role_name', 'plan_time', 'pyrus_stage', )
    

@admin.register(SystemServicePyrusForms)
class SystemServicePyrusFormsAdmin(admin.ModelAdmin):
    list_display = ('form', )
    filter_horizontal = ('system_service',  )

@admin.register(PyrusForms)
class PyrusFormsAdmin(admin.ModelAdmin):
    list_display = ('form_id', 'form_name', )
