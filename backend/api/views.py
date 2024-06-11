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