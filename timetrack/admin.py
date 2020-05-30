# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import (
    TimecardModel,
    TimecardStatusModel,
    StatusMasterModel,
    TimecardHistoryModel,
    TimecardSettingsModel,
    OrganizationModel,
    ProjectModel,
    InvitedUserModel
)
# Register your models here.


class TimecardModelAdmin(admin.ModelAdmin):

    list_display = ('clock_in', 'clock_out', 'created_on', 'employee', 'is_clocked_out')


class TimecardStatusModelAdmin(admin.ModelAdmin):

    list_display = ('timecard', 'status', 'is_approved', 'is_draft')


class TimecardHistoryModelAdmin(admin.ModelAdmin):

    list_display = ('timecard', 'employee', 'date1', 'work_time', 'brake_time', 'overtime', 'double_overtime', 'total_hours')


class TimecardSettingsModelAdmin(admin.ModelAdmin):
    pass


admin.site.register(TimecardModel, TimecardModelAdmin)
admin.site.register(TimecardStatusModel, TimecardStatusModelAdmin)
admin.site.register(TimecardHistoryModel, TimecardHistoryModelAdmin)
admin.site.register(TimecardSettingsModel, TimecardSettingsModelAdmin)
admin.site.register(StatusMasterModel)
admin.site.register(OrganizationModel)
admin.site.register(ProjectModel)
admin.site.register(InvitedUserModel)
