from timetrack.models import TimecardModel, TimecardStatusModel, TimecardHistoryModel, TimecardSettingsModel
from rest_framework import serializers
import datetime


class ChoicesSerializerField(serializers.SerializerMethodField):
    """
    A read-only field that return the representation of a model field with choices.
    """

    def to_representation(self, value):
        # sample: 'get_XXXX_display'
        method_name = 'get_{field_name}_display'.format(field_name=self.field_name)
        # retrieve instance method
        method = getattr(value, method_name)
        # finally use instance method to return result of get_XXXX_display()
        return method()

    def to_internal_value(self, data):
        pass


class ClockInSerializer(serializers.ModelSerializer):

    class Meta:
        model = TimecardModel
        fields = (
            'terminal_id',
            'latitude',
            'longitude',
            'clock_in_address',
            'employee',
            'clock_in',
            'project',
            'is_clocked_out',
            'created_on',
            'updated_on',
            'is_active',

        )


class ClockOutSerializer(serializers.ModelSerializer):

    class Meta:
        model = TimecardModel
        fields = (
            'terminal_id',
            'latitude',
            'longitude',
            'clock_out_address',
            'employee',
            'clock_out',
            'project',
            'is_clocked_out',
            'created_on',
            'updated_on',
            'is_active',

        )



class TimeCardModelSerializer(serializers.ModelSerializer):
    cost_code = serializers.SerializerMethodField()
    cost_code_description = serializers.SerializerMethodField()
    employee_name = serializers.SerializerMethodField()
    project_name = serializers.SerializerMethodField()

    class Meta:
        model = TimecardModel
        fields = (
            'id',
            'terminal_id',
            'latitude',
            'longitude',
            'clock_in_address',
            'clock_out_address',
            'employee_name',
            'employee',
            'clock_in',
            'clock_out',
            'project_name',
            'signature',
            'is_clocked_out',
            'cost_code',
            'cost_code_description',
            'created_on',
            'updated_on',
            'is_active',

        )

    def get_employee_name(self, instance):
        name = 'name here'
        return name

    def get_project_name(self, instance):
        project_name = 'project_name'
        return project_name

    def get_cost_code(self, obj):
        obj = 'Cost code here'
        return obj

    def get_cost_code_description(self, obj):
        obj = 'Cost code description here'
        return obj


class TimecardHistoryModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = TimecardHistoryModel
        fields = (
            'timecard',
            'employee',
            'date1',
            'work_time',
            'brake_time',
            'overtime',
            'double_overtime',
            'total_hours',
            'created_on',
            'updated_on',
            'is_active',
        )


class TimecardStatusModelSerialzier(serializers.ModelSerializer):

    timecard = TimeCardModelSerializer()

    class Meta:
        model = TimecardStatusModel
        fields = (
            'status',
            'is_approved',
            'is_draft',
            'created_on',
            'updated_on',
            'is_active',
            'timecard',
        )


# 12
class TimecardSettingsModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = TimecardSettingsModel
        fields = (

            'id',
            'start_time',
            'first_break_start',
            'first_break_end',
            'lunch_time',
            'lunch_end',
            'second_break_start',
            'second_break_end',
            'finish_time',
            'regular_hours',
            'grace_period',
            'overtime',
            'double_overtime',
            'total_hours',
            'typical_notes',
            'organization',

        )
