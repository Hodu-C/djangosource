from django.shortcuts import render
from .forms import RegisterForm

# Create your views here.
def user_register(request):
    """
    회원가입
    """
    #get(비어있는 Register) / post(사용자의 입력값이 RegisterForm)
    if request.method == "POST":
        user_form = RegisterForm(request.POST)
        
        if user_form.is_valid():
           user = user_form.save(commit=False) # 임시 저장
           #유효성 검증이 끝난 데이터 세팅
           user.set_password(user_form.cleaned_data['password'])
           #최종 저장
           user.save()
           return render(request, "registration/login.html")
           
            
    else:
        user_form = RegisterForm()
        
    return render(request, "user/register.html", {"user_form":user_form})