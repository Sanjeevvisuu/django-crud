from django.shortcuts import render

# Create your views here.
from .models import *
from .serializer import *
# Create your views here.
# restframe
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def get(request):
    stu = students.objects.all()
    serializer = students_serializer(stu, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_specific(request, id):
    stu = students.objects.get(id=id)
    serializer = students_serializer(stu)
    return Response(serializer.data)


@api_view(['DELETE'])
def delete(request, id):
    stu = students.objects.get(id=id)
    stu.delete()
    return Response({"sucess": "student deleted successfully"}, status=200)


@api_view(["PUT"])
def update(request, id):
    try:
        stu = students.objects.get(id=id)
        serializer = students_serializer(stu, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"sucess": "successfully updated "}, status=200)
        else:
            return Response({"fail": "fail  to  update "}, status=400)
    except students.DoesNotExist:
        return Response({"fail": "students does not exits "}, status=404)


@api_view(['POST'])
def create_api(request):
    new_stu = request.data
    serializer = students_serializer(data=new_stu)
    if serializer.is_valid():
        serializer.save()
        return Response({"sucess": "successfully created a new students"}, status=200)
    else:
        return Response(serializer.errors, status=404)
