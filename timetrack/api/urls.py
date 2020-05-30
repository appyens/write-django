from django.conf.urls import url, include
from . import views

urlpatterns = [
    # 1
    url(r'^(?P<org>[A-Za-z0-9]+)/summary/employee/(?P<emp_id>\d+)/$', views.GetEmployeeTimecardDetailsAPIView.as_view(), name='get_employee_timecards'),
    # 2
    url(r'^(?P<org>[A-Za-z0-9]+)/clock-in/employee/$', views.EmployeeClockIn.as_view(), name='employee_clock_in'),
    # 3
    url(r'^(?P<org>[A-Za-z0-9]+)/clock-out/employee/$', views.EmployeeClockOut.as_view(), name='employee_clock_out'),
    # 4
    url(r'^(?P<org>[A-Za-z0-9]+)/preview/employee/(?P<emp_id>\d+)/$', views.EmployeeTimecardPreview.as_view(), name='employee_timecard_preview'),
    # 5
    url(r'^(?P<org>[A-Za-z0-9]+)/submit/employee/(?P<emp_id>\d+)/$', views.EmployeeTimecardSubmit.as_view(), name='employee_timecard_submit'),
    # 6
    url(r'^(?P<org>[A-Za-z0-9]+)/summary/foreman/(?P<emp_id>\d+)/$', views.GetForemanTimecardDetailsAPIView.as_view(),
        name='get_foreman_timecards'),
    # 7
    url(r'^(?P<org>[A-Za-z0-9]+)/clock-in/foreman/$', views.ForemanClockIn.as_view(), name='foreman_clock_in'),
    # 8
    url(r'^(?P<org>[A-Za-z0-9]+)/clock-out/foreman/$', views.ForemanClockOut.as_view(), name='foreman_clock_out'),
    # 9
    url(r'^(?P<org>[A-Za-z0-9]+)/preview/foreman/(?P<emp_id>\d+)/$', views.ForemanTimecardPreview.as_view(),
        name='foreman_timecard_preview'),
    # 10
    url(r'^(?P<org>[A-Za-z0-9]+)/submit/foreman/(?P<emp_id>\d+)/$', views.ForemanTimecardSubmit.as_view(),
        name='foreman_timecard_submit'),

]
