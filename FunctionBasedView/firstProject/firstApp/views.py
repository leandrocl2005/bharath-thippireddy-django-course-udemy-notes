from firstApp.serializers import EmployeeSerializer

# from django.http import JsonResponse

from firstApp.models import Employee

from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
"""
def employeeView(request):
    data = Employee.objects.all()
    response = {'employees': list(data.values('name', 'sal'))}
    return JsonResponse(response)
"""


@api_view(['GET', 'POST'])
def employee_list(request):

    if request.method == "GET":
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def employee_detail(request, pk):
    try:
        employee = Employee.objects.get(pk=pk)
    except Employee.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
