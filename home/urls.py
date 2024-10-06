# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('quiz/', views.quiz, name='quiz'),
    path('get_quiz/', views.get_quiz, name='get_quiz'),  # Add this line
]

