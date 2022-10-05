from django.shortcuts import redirect, render,get_object_or_404
from django.core.paginator import Paginator

from .models import Question
from .forms import QuestionForm, AnswerForm

# Create your views here.
def index(request):
    """
    Question 추출
    """
    # 사용자가 요청한 페이지 값 가져오기
    page = request.GET.get("page", 1)
    
    # 전체 목록 추출
    questions_list = Question.objects.order_by("-created_at")
    
    # 전체 목록 안에서 사용자가 요청한 페이지에 대한 목록만 전송
    paginator = Paginator(questions_list, 10)
    question_list = paginator.get_page(page)

    return render(request, "board/question_list.html", {"question_list": question_list})

def question_detail(request, question_id):
    """
    Question 상세 내용 추출
    """
    question = get_object_or_404(Question, id=question_id)
    return render(request, 'board/question_detail.html', {"question":question})


def question_create(request):
    """
    Question 등록
    """
    if request.method=="POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("board:index")
    
    else:
        form = QuestionForm()
        
        
    return render(request, "board/question_create.html", {"form":form})
    
def answer_create(request, question_id):
    """
    Answer 등록
    """
    question = get_object_or_404(Question, id=question_id)
    if request.method=="POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            answer.save()
            return redirect("board:question_detail", question_id=question_id)
    else:
        form = AnswerForm()
        
    return render(request, "board/question_detail.html", {"form":form, "question":question})
        