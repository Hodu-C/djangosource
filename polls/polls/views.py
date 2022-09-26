from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question

# Create your views here.
def index(request):
    return HttpResponse("index")


def detail(request, quesion_id):
    question = get_object_or_404(Question, pk=quesion_id)
    
    return render(request, "detail.html", {"question":question})

def results(request, quesion_id):
    return HttpResponse("you're looking at the results of question %s " %(quesion_id))

def vote(request, quesion_id):
    return HttpResponse("you're voting on question %s " %(quesion_id))