from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	# return HttpResponse("my_to_do_appp first page")
	return render(request, 'my_to_do_app/index.html')

# render html 파일을 사용자에게 보여주려면 render 함수
# request가 user나 session 같은 중요한 값들 전달
# 사용자가 특정 url에 접근해서 index 함수를 실행할때 기본적으로 request 를 받아와 user나 session 값 참조 

def createTodo(request):
	return HttpResponse("Create Todo를 할거야!")