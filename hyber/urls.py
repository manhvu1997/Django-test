from django.urls import path
from . import views

urlpatterns = [
    path('infor/', views.index3, name='infor')
]