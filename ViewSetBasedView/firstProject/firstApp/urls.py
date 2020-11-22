from django.urls import path, include
from firstApp import views

# ViewSet class based views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('employees', views.EmployeeViewSet)

urlpatterns = [path('', include(router.urls))]

# ApiView/Generics/mixins class based views
# urlpatterns = [
#    path('employees/', views.EmployeeList.as_view()),
#    path('employees/<int:pk>/', views.EmployeeDetail.as_view())
# ]

# function based views
# urlpatterns = [
# path('employees/', views.employee_list),
# path('employees/<int:pk>/', views.employee_detail)
# ]
