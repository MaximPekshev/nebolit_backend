from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import get_doctors, get_doctor_shedule
from .views import get_doctor_day_shedule, get_doctor_detail
from .views import make_an_appointment, send_phone_to_check, check_phone



urlpatterns = [
	path('doctor-list/', get_doctors, name='get_doctors'),
	path('doctor-detail/<str:uid>/', get_doctor_detail, name='get_doctor_detail'),
	path('doc-shedule/<str:uid>/', get_doctor_shedule, name='get_doctor_shedule'),
	path('doc-day-shedule/<str:uid>/', get_doctor_day_shedule, name='get_doctor_day_shedule'),
	path('make-an-appointment/<str:uid>/', make_an_appointment, name='make_an_appointment'),
	path('send-phone-to-check/', send_phone_to_check, name='send_phone_to_check'),
	path('check-phone/', check_phone, name='check_phone'),
]