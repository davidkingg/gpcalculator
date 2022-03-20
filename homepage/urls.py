from urllib.parse import urlparse
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('login',views.login, name='login'),
    path('register',views.register, name='register'),
    path('logout',views.logout, name='logout'),
    path('register2',views.register2),
    path('courses',views.courses, name='courses'),
    path('userland',views.course_addition, name='userland'),
    path('cgpa',views.cgpa, name='cgpa'),
    path('GPpage',views.gp_page, name='GPpage'),
]
