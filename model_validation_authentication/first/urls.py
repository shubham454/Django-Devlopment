from django.urls import path
from first import views

urlpatterns = [
    path('add/',views.EmployeeAdd.as_view()),
    path('list/',views.EmployeeRead.as_view()),
    path('delete/<int:id>/',views.EmloyeeDelete.as_view()),
    path('update/<int:id>/',views.EmployeeUpdate.as_view()),
    path('login/',views.LoginEmployee.as_view()),
    path('img/',views.saveimg)
]
