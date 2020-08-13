from django.urls import path,include
from first import views

urlpatterns=[
path('',views.home_page_view),
path('java/',views.java_exam_view),
path('python/',views.python_exam_view),
path('aptitude/',views.aptitude_exam_view),
# path('/logout', views.logout_view)
]
