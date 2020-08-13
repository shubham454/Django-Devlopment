from django.urls import path
from appone import views

urlpatterns = [
    #path('college/',views.college_view),
    path('uni/',views.add_uni),
    path('col/',views.add_col),
    path('index/', views.index_view),
    path('showcolg/', views.show_colg),
    path('showuni/', views.show_uni),
]
