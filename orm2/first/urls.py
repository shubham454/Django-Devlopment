from django.urls import path, include
from first import views

urlpatterns = [
    path('all/', views.all_dog),
    path('lt/', views.lt_method),
    path('count/', views.count),
    path('in/', views.in_method),
    path('gt/', views.gt_method),
    path('value/', views.value),
]
