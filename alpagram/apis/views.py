from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from users.forms import RegisterForm
from django.contrib.auth import authenticate, login

# Create your views here.


class BaseView(View):
    """
    요청에 대해서 JsonResponse로 응답하는 View
    """
    @staticmethod
    def response(result={}, status=200):

        # key, value
        return JsonResponse(result, status=status)


class UserCreateView(BaseView):
    """
    사용자 생성
    """

    # request 요청이 들어왔을 때 get or post 나 분별
    def dispatch(self, request, *args, **kwargs):
        return super(UserCreateView, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()

            # 로그인 처리
            login_user = authenticate(
                usernmae=form.cleaned_data["email"],
                passowrd=form.cleaned_data["password"],
            )
            login(request, login_user)

            return self.response({"error": False, "message": "success"})
        else:
            # 검증통과 x 상황 - email 중복
            return self.response({
                "error": True,
                "message": form.errors
            },
                                 status=400)
