# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils import timezone

# Create your models here.


class OrganizationModel(models.Model):
    admin = models.ForeignKey(User)
    # language = models.ForeignKey(LanguageModel)
    # time_zone = models.ForeignKey(TimeZoneModel)
    name = models.CharField("Organization Name", max_length=100)
    description = models.CharField("Organization Description", max_length=200, blank=True, null=True)
    created = models.DateTimeField('Created Date', auto_now_add=True)
    updated = models.DateTimeField('Updated', auto_now=True)
    created_by = models.ForeignKey(User, related_name='%s+' % "Created By")
    update_by = models.ForeignKey(User, related_name='%s+' % "Updated By")
    is_active = models.BooleanField(default=True)
    sub_admins = models.ManyToManyField(User, related_name='SubAdmin')
    #    free tool integration fields
    is_using_freetool = models.BooleanField(default=False, )
    freetool = models.CharField(null=True, blank=True, max_length=100)
    is_active_costcode = models.BooleanField(default=False, )

    def __unicode__(self):
        return self.name


class ProjectModel(models.Model):
    slug_field = models.SlugField(max_length=10, blank=True, db_index=True)
    code = models.CharField(max_length=15, db_index=True)
    organization = models.ForeignKey(OrganizationModel)
    creator = models.ForeignKey(User)
    is_budget_freeze = models.BooleanField("budget status, freeze or not", default=False)
    # country = models.ForeignKey(CountryModel, null=True, blank=True)
    zip_code = models.CharField(max_length=10, null=True, blank=True)
    is_active = models.BooleanField("Project status, active or not", default=True)
    start_date = models.DateTimeField(auto_now_add=True, blank=True)
    end_date = models.DateTimeField("end date", null=True, blank=True)
    # role = models.ForeignKey(RoleModel, db_index=True, null=True, blank=True)
    # base_value=models.CharField(max_length=30, db_index=True, null=True, blank=True, default=0)
    base_value = models.BigIntegerField(db_index=True, null=True, blank=True, default=0)
    is_delete = models.BooleanField("Is delete", default=False)
    deleted_on = models.DateTimeField("delete date", null=True, blank=True)

    def __unicode__(self):
        return self.code


class TimecardModel(models.Model):

    terminal_id = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(max_length=16, blank=True, null=True)
    longitude = models.FloatField(max_length=16, blank=True, null=True)
    clock_in_address = models.CharField(max_length=256, blank=True)
    clock_out_address = models.CharField(max_length=256, blank=True)
    employee = models.ForeignKey(User)
    clock_in = models.DateTimeField(blank=True, null=True, editable=True)
    clock_out = models.DateTimeField(blank=True, null=True)
    project = models.ForeignKey(ProjectModel, null=True)
    signature = models.FileField(blank=True, null=True)
    is_clocked_out = models.BooleanField(blank=True, default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return str(self.id)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.clock_out:
            self.is_clocked_out = True
            super(TimecardModel, self).save()
        super(TimecardModel, self).save()

    def clockout(self):
        self.clock_out = timezone.now()
        self.is_clocked_out = True
        self.save()
        return self.is_clocked_out


class TimecardHistoryModel(models.Model):

    timecard = models.ForeignKey(TimecardModel)
    employee = models.ForeignKey(User)
    date1 = models.DateTimeField()
    work_time = models.FloatField()
    brake_time = models.FloatField()
    overtime = models.FloatField(default='4')
    double_overtime = models.FloatField(default='5')
    total_hours = models.DecimalField(decimal_places=2, max_digits=5, default='08.00')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return str(self.date1)


class StatusMasterModel(models.Model):

    """
        TIMECARD_STATUS = (
        ("1", "Created"),
        ("2", "Updated"),
        ("3", "Submitted"),
        ("4", "Approved"),
    )
    """
    name = models.CharField(max_length=128)
    created_on = models.DateTimeField()
    updated_on = models.DateTimeField()
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return str(self.name)


class TimecardStatusModel(models.Model):
    """
        Time card Details Translation
    """
    timecard = models.ForeignKey(TimecardModel)
    status = models.ForeignKey(StatusMasterModel)
    is_approved = models.BooleanField(default=False)
    is_draft = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return str(self.id)


class TimecardSettingsModel(models.Model):
    """
        Settings for Timecard Tool.....
    """
    start_time = models.TimeField(default='07:00')
    first_break_start = models.TimeField(default='09:30')
    first_break_end = models.TimeField(default='09:40')
    lunch_time = models.TimeField(default='12:00')
    lunch_end = models.TimeField(default='12:30')
    second_break_start = models.TimeField(default='00:00')
    second_break_end = models.TimeField(default='00:00')
    finish_time = models.TimeField(default='02:30')
    regular_hours = models.TimeField(default='08:00')
    grace_period = models.FloatField(default='5')
    overtime = models.FloatField(default='5')
    double_overtime = models.FloatField(default='5')
    total_hours = models.DecimalField(max_digits=5, decimal_places=2)
    typical_notes = models.CharField(max_length=1000, default='By signing here, the user acknowledges that this '
                                                              'time card is accurate. The user also acknowledges that '
                                                              'their password or bar code entry may be used as their '
                                                              'digital signature for entries made into the system')
    organization = models.ForeignKey(OrganizationModel)

    def __unicode__(self):
        return str(self.organization.id)


class InvitedUserModel(models.Model):
    """ project-company wise users and their role """
    # role = models.ForeignKey(RoleModel, blank=True, null=True)
    user = models.ForeignKey(User, default=1)
    user_company = models.ForeignKey(OrganizationModel)
    is_active = models.BooleanField(default=True)
    project = models.ForeignKey(ProjectModel)
    is_invite = models.IntegerField(default=0)
    is_response = models.IntegerField(default=0)
    invited_date = models.DateTimeField(auto_now_add=True, blank=True)
    is_perm_set = models.BooleanField(default=False)

    def __unicode__(self):
        return self.user.username
