from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('category/5/', index),
    path('category/<int:category_id>/', get_category, name='category'),
]
