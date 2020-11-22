from django.urls import path

from firstApp import views

# ApiView class based views
urlpatterns = [
    path('employees/', views.EmployeeList.as_view()),
    path('employees/<int:pk>/', views.EmployeeDetail.as_view())
]

# function based views
# urlpatterns = [
# path('employees/', views.employee_list),
# path('employees/<int:pk>/', views.employee_detail)
# ]
