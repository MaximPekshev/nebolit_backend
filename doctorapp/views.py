from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import generics
import requests
import json
import time
import random
from .models import PhoneCheck

from decouple import config 


def get_all_info(request):
	url = 'https://1c.nebolitonline.ru/bit_med/hs/annasoft/api/v1/getAllInfo'
	header = {'Authorization' : config('1C_API_SECRET_KEY')}
	answer = requests.get(url, headers=header)
	return HttpResponse(answer)

def get_doctors(request):

	url = 'https://1c.nebolitonline.ru/bit_med/hs/annasoft/api/v1/getDoctors'
	header = {'Authorization' : config('1C_API_SECRET_KEY')}
	answer = requests.get(url, headers=header)
	return HttpResponse(answer)

def get_doctor_shedule(request, uid):
	if uid:
		url = 'https://1c.nebolitonline.ru/bit_med/hs/annasoft/api/v1/getDoctorSchedule?doctor={}'.format(uid)
		header = {'Authorization' : config('1C_API_SECRET_KEY')}
		answer = requests.get(url, headers=header)
		
		return HttpResponse(answer)


def get_doctor_day_shedule(request, uid):

	if request.method == 'GET':
		if uid:

			date = request.GET.get('date')

			url = 'https://1c.nebolitonline.ru/bit_med/hs/annasoft/api/v1/getDoctorTime?doctor={}&date={}'.format(uid, date)
			header = {'Authorization' : config('1C_API_SECRET_KEY')}
			answer = requests.get(url, headers=header)
			return HttpResponse(answer)


def get_doctor_detail(request, uid):

	if request.method == 'GET':
		if uid:
			url = 'https://1c.nebolitonline.ru/bit_med/hs/annasoft/api/v1/getDoctor?doctor={}'.format(uid)
			header = {'Authorization' : config('1C_API_SECRET_KEY')}
			answer = requests.get(url, headers=header)
			return HttpResponse(answer)


def make_an_appointment(request, uid):
	
	if request.method == 'GET':

		if uid:

			url = 'https://1c.nebolitonline.ru/bit_med/hs/annasoft/api/v1/setRecord'
			header = {'Authorization' : config('1C_API_SECRET_KEY')}

			input_date = request.GET.get('date')
			date = input_date.replace('-','') + '000000'
			input_time = request.GET.get('time')
			input_name = request.GET.get('name')
			input_surname = request.GET.get('surname')
			input_phone = request.GET.get('phone')
			phone = "7" +  input_phone.replace("(","").replace(")","").replace(" ","").replace("-", "")

			input_date_of_birth = request.GET.get('date_of_birth')
			date_of_birth = input_date_of_birth.replace('-','') + '000000'
			data = {
				"fields": {
					"doctor"  : uid, 
	                "date" : input_date + '000000',
	                "time" : input_time,
	                "name" : input_name,
	                "surname" : input_surname,
	                "phone" : phone,
	                "date_of_birth" : date_of_birth
	            }
			}

			# print(json.dumps(data))

			answer = requests.post(url, headers=header, data=json.dumps(data))

			return HttpResponse('200')

	return HttpResponse('500')	



def send_phone_to_check(request):

	if request.method == 'GET':

		input_phone = request.GET.get('phone')
		phone = "7" +  input_phone.replace("(","").replace(")","").replace(" ","").replace("-", "")

		a = random.sample(range(10),3)
		code = int(str(random.randint(1,9)) + str(a[0]) + str(a[1]) + str(a[2]))
		if phone and code:
			phnChck = PhoneCheck(phone=phone, code=code)
			phnChck.save()
			# print(phnChck.code)

			sms_text = 'НЕБОЛИТ. Код для входа {}'.format(code)

			url = 'https://gateway.api.sc/get/?user={0}&pwd={1}&sadr={2}&dadr={3}&text={4}'.format(
						config('STREAM_LOGIN'),
						config('STREAM_API_PASS'),
						config('STREAM_SADR'),
						phone,
						sms_text,
					)

			answer = requests.get(url)

			return HttpResponse('200')
		else:
			return HttpResponse('500')

		

def check_phone(request):

	if request.method == 'GET':

		phone = request.GET.get('phone')
		input_phone = "7" +  phone.replace("(","").replace(")","").replace(" ","").replace("-", "")

		input_code = request.GET.get('code')

		if input_phone and input_code:

			phone = PhoneCheck.objects.filter(phone=input_phone, cleared=False).last()

			if phone.code == input_code:

				phone.cleared = True
				phone.save()
				return HttpResponse('200')
				

			else:
				
				return HttpResponse('500')	

				



		