from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.http import HttpResponse
from .models import Question

# def index(request):
#     # 등록 날짜를 기준으로 최신 질문 5개 추출
#     # -pub_date : 내림차순 정렬, pub_date : 오름차순 정렬
#     lastest_question_list = Question.objects.order_by("-pub_date")[:5]

#     # output = ", ".join([q.question_text for q in lastest_question_list])
#     # return HttpResponse(output)

#     # index.html 보여주기 + lastest_question_list
#     return render(request, "index.html", {"lastest_question_list":lastest_question_list})


# # 함수형 뷰
# def detail(request,question_id):
#     #  return HttpResponse("You're looking at the question %s" % (question_id))

#     question = get_object_or_404(Question,pk=question_id)

#     return render(request, "detail.html", {"question":question})


# def results(request,question_id):
#     return HttpResponse("You're looking at the results of question %s" % (question_id))

def vote(request,question_id):
    """
    투표수 증가
    """
    # return HttpResponse("You're voting on question %s" % (question_id))

    question = get_object_or_404(Question, pk=question_id)

    if request.method == "POST":
        # 사용자의 투표 값 가져오기
        try:
            selected_choice = question.choice_set.get(pk=request.POST['choice'])

        except KeyError as e:
            return render(request,"polls/detail.html",{"question":question, "error_message":"값을 선택하지 않았습니다"})

        else:
            selected_choice.votes += 1
            selected_choice.save()
            #함수형 뷰
            #return redirect("results",question_id=question_id)      
            
            #클래스 뷰
            return redirect("results", pk=question_id)
        
        
#제네릭 뷰
#template_name : <app_name>/<model_name>_list.html 템플릿을 사용함
#context_object_name : 모델을 담는 이름(기본값으로 <model_name>_list 나 object_list 사용가능)
class IndexView(ListView):
    """Index() 역할"""
    template_name = "polls/index.html"
    context_object_name = "lastest_question_list"
    
    # model = Question
    def get_queryset(self):
        return Question.objects.order_by("-pub_date")[:5]
    
#template_name : <app_name>/<model_name>_detail.html 템플릿을 사용함

class QuestionDetailView(DetailView):
    """Detail()"""
    model = Question
    template_name = "polls/detail.html"
    
class QuestionResultView(DetailView):
    """result()"""
    model = Question
    template_name = "polls/results.html"
    
    