from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

from .models import Photo
# Create your views here.
#함수형 뷰
def home(request):
    # HttpResponse : 응답 객체
    # 1) 문자열을 담아서 리턴
    # 2) 특정 페이지를 리턴
    return HttpResponse("INDEX")


def photo_list(request):
    # HttpResponse : 응답 객체
    # 1) 문자열을 담아서 리턴
    # 2) 특정 페이지를 리턴
    
    # 사진목록 추출한 후 목록을 보내야 함
    # select * from photo_photo; -> Django
    photos = Photo.objects.all()
    
    #return 결과는 QuerySet 형태로 나옴
    return render(request, "photo_list.html",{"photos":photos})

def photo_post(request):
    return render(request, "photo_post.html")
