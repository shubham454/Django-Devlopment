from django.urls import path
from first import views

urlpatterns = [
    path('student/', views.student_info),
]
