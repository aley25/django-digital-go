from django.urls import path
from . import views


#urlconf
urlpatterns = [
    path('', views.index),
    path('hello/', views.say_hello),
    path('counter/', views.word_counter),
    path('counter/result/', views.result),
]