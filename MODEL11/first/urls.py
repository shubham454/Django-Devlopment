from django.urls import path
from first import views

urlpatterns = [
    path('list/',views.GetBankData.as_view()),
    path('add/', views.AddBankData.as_view()),
    path('<int:ano>/', views.DeleteView.as_view()),
    path('update/<int:ano>/', views.UpdateView.as_view()),
]
