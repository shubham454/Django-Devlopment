from django.urls import path
from first import views

urlpatterns = [
    path('user/', views.User_registration),
    path('success/', views.success_view)
]
