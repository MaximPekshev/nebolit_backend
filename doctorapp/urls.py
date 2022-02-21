from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import make_an_appointment, send_phone_to_check, check_phone, send_alert
from .views import get_all_info, get_doctor_info



urlpatterns = [
	path('getAllInfo/', get_all_info, name='get_all_info'),
	path('getDoctorInfo/<str:uid>/', get_doctor_info, name='get_doctor_info'),
	path('make-an-appointment/<str:uid>/', make_an_appointment, name='make_an_appointment'),
	path('send-phone-to-check/', send_phone_to_check, name='send_phone_to_check'),
	path('check-phone/', check_phone, name='check_phone'),
	path('send-alert/', send_alert, name='send_alert'),
]