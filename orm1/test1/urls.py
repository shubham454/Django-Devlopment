from django.urls import path
from test1 import views

urlpatterns = [
    path('allemp/', views.all_employee),
    path('filter1/', views.filter1),
    path('filter2/', views.filter2),
    path('filter3/', views.filter3),
    path('filter4/', views.filter4),
    path('filter5/', views.filter5),
]
