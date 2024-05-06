from django.urls import path
from .views import get_info,get_name,get_surname,get_country,get_email,get_phone,get_university,get_faculty,get_gender

urlpatterns = [
    path('app_url/', get_info,name='app'),
    path('name_url/',get_name,name='name'),
    path('surname_url/',get_surname,name='surname'),
    path('country_url/',get_country,name='country'),
    path('email_url/',get_email,name='email'),
    path('phone_url/',get_phone,name='phone'),
    path('university_url/',get_university,name='university'),
    path('faculty_url/',get_faculty,name='faculty'),
    path('gender_url/',get_gender,name='gender'),
]