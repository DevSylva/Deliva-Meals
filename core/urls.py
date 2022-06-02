from django.urls import path
from core.views import *


app_name = "core"

urlpatterns = [
    path("food/", food, name="food"),
    path("food/<int:id>/", food_detail, name="food_detail"),
    path("food/category/<str:cat>/", filter_by_category, name="filter_by_category"),
]
