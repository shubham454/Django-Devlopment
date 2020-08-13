from django.urls import path
from first import views

urlpatterns = [
    path('all/', views.all_emp),
    path('add/',views.add_emp),
    path('delete/<int:id>/', views.delete_emp),
    path('update/<int:id>/',views.update_emp),
    ]
