from django.urls import path
from testapp import views

urlpatterns = [
    path('create/', views.BeerCreateView.as_view(), name = 'create'),
    path('list/',views.BeerListView.as_view(), name = 'list'),
    path('<int:pk>/',views.BeerDetailView.as_view(),name='detail'),
    path('update/<int:pk>/',views.BeerUpdateView.as_view(),name='update'),
    path('delete/<int:pk>/',views.BeerDeleteView.as_view(),name='delete'),
]
