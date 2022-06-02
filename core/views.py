from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import logout
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser
from rest_framework.decorators import parser_classes
from core.models import *
from core.serializers import *



# Create your views here.
@api_view(["POST"])
def register(request):
    if request.method == "POST":
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser])
@swagger_auto_schema(request_body=FoodSerializer)
def food(request):
    if request.method == "GET":
        food = Food.objects.all()
        if food.count() >= 1:
            serializer = FoodSerializer(food, many=True)
            data = {"status": "Ok", "count": food.count(), "data": serializer.data}
            return Response(data, status=status.HTTP_200_OK)
        else:
            data = {"status": "ok", "count": food.count(), "data": []}
            return Response(data, status=status.HTTP_200_OK)

    elif request.method == "POST":
        serializer = FoodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "status": "ok",
                "message": "food created",
                "data": serializer.data
            }
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            data = {
                "status": "error", 
                "data": serializer.errors
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)



@api_view(["GET", "PUT", "DELETE"])
@permission_classes([IsAuthenticated])
@swagger_auto_schema(request_body=FoodSerializer)
def food_detail(request, id):
    try:
        food = Food.objects.get(id=id)
    except Food.DoesNotExist:
        return Response("Food does not exist", status=status.HTTP_200_OK)

    if request.method == "GET":
        serializer = FoodSerializer(food)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == "PUT":
        serializer = FoodSerializer(food, data=request.data) 
        if serializer.is_valid(): 
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_200_OK) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 

    elif request.method == "DELETE":
        food.delete()
        return Response("Food deleted", status=status.HTTP_200_OK)



@api_view(["GET"])
@permission_classes([IsAuthenticated])
def filter_by_category(request, cat):
    try:
        food = Food.objects.filter(category=cat.title())
    except Food.DoesNotExist:
        return Response("Category does not exist", status=status.HTTP_200_OK)

    if request.method == "GET":
        serializer = FoodSerializer(food, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    