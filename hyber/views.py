from django.shortcuts import render
from django.http import HttpResponse

def index3(request):
    content = HttpResponse("<h1>My information</h1><br><div>sdt: 0971829580</div><div>address: 74/195 Tran Cung, Co Nhue 1, Bac Tu Liem, Ha Noi</div><div>fb:</div>")
    return content

# Create your views here.
