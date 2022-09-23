from django import forms
from django.core.exceptions import ValidationError
from .models import Musician
# 폼(Form)의 종류 : HTML의 <form> 태그 || <form> 을 만들어내는 Form 클래스 || 서버로 제출된 구조화된 데이터
# 장고의 폼 처리 기능
# 1) 폼 생성에 필요한 데이터를 폼 클래스로 구조화
# 2) 폼 클래스의 데이터를 렌더링하여 HTML 폼 생성
# 3) 사용자로부터 제출된 폼과 데이터를 수신하고 처리

# 장고의 폼 클래스 생성 - forms.Form 상속 || forms.ModelForm

class NameForm(forms.Form):
    name = forms.CharField(max_length=20,label="Your name")
    
    # def clean_name(self) :
        
    #     cleaned_data = super().clean()
        
    #     #추가 검증
    #     name = cleaned_data.get('name') #cleaned_data['name']
        
    #     if name != "홍길동":
    #         raise ValidationError("이름을 확인해주세요")
    
    def clean(self) :
        
        cleaned_data = super().clean()
        
        #추가 검증
        name = cleaned_data.get('name') #cleaned_data['name']
        
        
        if name != "홍길동":
            self.add_error("name","입력값을 확인해주세요") #clean 함수를 쓸 시 
            raise ValidationError("이름을 확인해주세요") #non_field 에러로 인식, clean_[얻어온클린데이터 이름]
        
class MusicianForm(forms.ModelForm):
    #모델폼 상속시 Meta 필수
    class Meta:
        model = Musician
        # exclude = ['instrument']  -- all 사용시 제외가능
        # fields = ['first_name','last_name'] 와 같이 나열도 가능
        fields = "__all__"
        

    