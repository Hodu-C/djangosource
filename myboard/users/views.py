from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from .forms import UserForm

# Create your views here.
def signup(request):
    if request.method=="POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            
            #return redirect("users:login")
            
            #로그인 처리까지 구현
            username = form.cleaned_data.get("username")
            passowrd = form.cleaned_data.get("password1")
            
            user = authenticate(request,username=username, passowrd=passowrd)
            if user is not None:
                #로그인 정보 세션에 담아줌
                login(request, user)
            return redirect("board:index")
    else:
        form = UserForm()
    
    return render(request, "users/register.html", {"form":form})