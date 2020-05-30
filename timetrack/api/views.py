from __builtin__ import super
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth.models import User
from django.http import JsonResponse
import datetime
from .serializers import (
    ClockInSerializer,
    ClockOutSerializer,
    TimeCardModelSerializer,
    TimecardStatusModelSerialzier,
    TimecardSettingsModelSerializer,
)
from timetrack.models import (
    TimecardModel,
    TimecardStatusModel,
    TimecardHistoryModel,
    TimecardSettingsModel,
    OrganizationModel,
    ProjectModel,
    InvitedUserModel
)


# 1
class GetEmployeeTimecardDetailsAPIView(APIView):

    def get(self, request, org=None, emp_id=None):
        # session = Session.objects.get(session_key=request.META.get('HTTP_SESSIONID'))
        # uid = session.get_decoded().get('_auth_user_id')
        user = request.user
        print user
        response = None
        # if user.is_authenticated():
        flag = not None
        timecard = TimecardStatusModel.objects.filter(status__name='Submitted')
        serializer = TimecardStatusModelSerialzier(timecard, many=True)
        response = {'message': serializer.data, 'success': '1'}
        return Response(response, status=status.HTTP_200_OK)


# 2
class EmployeeClockIn(APIView):

    def post(self, request, org=None):
        data = request.data
        serializer = ClockInSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            response = {'message': serializer.data, 'success': '1'}
            return Response(response, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 3
class EmployeeClockOut(APIView):

    def post(self, request, org=None):
        data = request.data
        serializer = ClockOutSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            response = {'message': serializer.data, 'success': '1'}
            return Response(response, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 4
class EmployeeTimecardPreview(APIView):

    def get(self, request, org=None, emp_id=None):
        first = TimecardStatusModel.objects.filter(status__name='Updated', created_on=datetime.date.today()).first()
        last = TimecardStatusModel.objects.filter(status__name='Updated', created_on=datetime.date.today()).last()

        # serializer = TimecardStatusModelSerialzier(timecard, many=True)
        # response = {'message': serializer.data, 'success': '1'}
        # return Response(response, status=status.HTTP_200_OK)


# 5
class EmployeeTimecardSubmit(APIView):

    def post(self, request, org=None):
        data = request.data
        serializer = ClockOutSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            response = {'message': serializer.data, 'success': '1'}
            return Response(response, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 6
class GetForemanTimecardDetailsAPIView(APIView):

    def get(self, request, org=None, emp_id=None):
        # session = Session.objects.get(session_key=request.META.get('HTTP_SESSIONID'))
        # uid = session.get_decoded().get('_auth_user_id')
        user = request.user
        print user
        response = None
        # if user.is_authenticated():
        flag = not None
        timecard = TimecardStatusModel.objects.filter(status__name='Submitted')
        serializer = TimecardStatusModelSerialzier(timecard, many=True)
        response = {'message': serializer.data, 'success': '1'}
        return Response(response, status=status.HTTP_200_OK)


# 7
class ForemanClockIn(APIView):

    def post(self, request, org=None):
        data = request.data
        serializer = ClockInSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            response = {'message': serializer.data, 'success': '1'}
            return Response(response, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 8
class ForemanClockOut(APIView):

    def post(self, request, org=None):
        data = request.data
        serializer = ClockOutSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            response = {'message': serializer.data, 'success': '1'}
            return Response(response, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 9
class ForemanTimecardPreview(APIView):

    def get(self, request, org=None, emp_id=None):
        first = TimecardStatusModel.objects.filter(status__name='Updated', created_on=datetime.date.today()).first()
        last = TimecardStatusModel.objects.filter(status__name='Updated', created_on=datetime.date.today()).last()

        # serializer = TimecardStatusModelSerialzier(timecard, many=True)
        # response = {'message': serializer.data, 'success': '1'}
        # return Response(response, status=status.HTTP_200_OK)


# 10
class ForemanTimecardSubmit(APIView):

    def post(self, request, org=None):
        data = request.data
        serializer = ClockOutSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            response = {'message': serializer.data, 'success': '1'}
            return Response(response, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
