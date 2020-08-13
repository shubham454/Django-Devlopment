from django.urls import path
from first import views

urlpatterns = [
    path('all/', views.all_view),
    path('add/', views.add_view),
    path('one/',views.Name.as_view()),
    path('two/',views.Name.as_view()),    
]
