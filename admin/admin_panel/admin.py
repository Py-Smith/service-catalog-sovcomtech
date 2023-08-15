from django.contrib import admin

from .models import (PyrusForms, PyrusUsers, Service, System, SystemAlias,
                     SystemCategory, SystemService, SystemServiceMainTeams,
                     SystemServicePyrusForms, SystemServiceСompetenceTeams,
                     TimeTable, TimeTableDate)


@admin.register(SystemCategory)
class SystemCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', )

    list_filter = ('name', )

    search_fields = ('name', 'description', )


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
    filter_horizontal = ('system_service', )


@admin.register(PyrusForms)
class PyrusFormsAdmin(admin.ModelAdmin):
    list_display = ('form_id', 'form_name', )


class TimeTableDateInline(admin.TabularInline):
    model = TimeTableDate
    list_display = ('date', 'is_work', 'week', 'year', 'qr', 'month', )


@admin.register(TimeTable)
class TimeTableAdmin(admin.ModelAdmin):
    inlines = (TimeTableDateInline, )
    list_display = ('name', 'description', )


@admin.register(PyrusUsers)
class PyrusUsersAdmin(admin.ModelAdmin):
    list_display = ('pyrus_id', 'email', 'username', 'department', 'management', 'divizion', )
