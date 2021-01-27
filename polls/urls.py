from django.urls import path
from . import views

urlpatterns = [
    path('polls/', views.index, name="index"),
    path('manh/',views.index1, name="mr"),
    path('mrmanh/',views.index2, name="mrmanh"),
    path('manhvu/',views.index3, name="manhvu"),
    path('results/<int:questionid>/',views.results, name="results"),
    path('<int:questionid>/',views.detail, name="detail"),
    path('<int:questionid>/vote/',views.vote, name="vote"),
    path('index4/',views.index4, name='index4')
]