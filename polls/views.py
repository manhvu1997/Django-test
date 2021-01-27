from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello mấy cưng")
def index1(request):
    return HttpResponse("<h1>Hello I'm Mrchu</h1>")
def index2(request):
    return HttpResponse("<h1>Hello I'm Mrchi</h1><h2>Nice to meet you</h2><p>Practice pythondjango</p>")
def index3(request):
    character = "HANDSOME"
    item = ["plane","laptop","touchpad","television","bridge","much money"]
    context = {"mycharacter":character,"item":item}
    return render(request,"polls/index.html",context)
def detail(request,questionid):
    response = "You are looking at question %s."
    return HttpResponse(response % questionid)
def results(request,questionid):
    return HttpResponse("You are looking at the results of question %s." % questionid)
def vote(request,questionid):
    return HttpResponse("You are voting on question %s." % questionid)
def index4(request):
    questionlist = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.questiontext for q in questionlist])
    return HttpResponse(output)