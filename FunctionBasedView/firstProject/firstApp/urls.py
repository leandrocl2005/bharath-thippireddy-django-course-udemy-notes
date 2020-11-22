from django.urls import path

from firstApp import views

urlpatterns = [
    path('employees/', views.employee_list),
    path('employees/<int:pk>/', views.employee_detail)
]
