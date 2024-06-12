from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Employee
from .serializers import EmployeeSerializer


@api_view(['GET', 'POST'])
def welcome(request):
    data = request.data
    print(data)
    return Response('Welcome to Django Rest Framework')


@api_view(['GET'])
def getEmployee(request):
    employee = Employee.objects.all()
    print(employee)
    serializer = EmployeeSerializer(employee, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def addEmployee(request):
    newEmployee = request.data
    serializer = EmployeeSerializer(data=newEmployee, many=True)
    if serializer.is_valid():
        serializer.save()
        return Response(f"Employee successfully added {serializer.data}")
    return Response(serializer.errors)
