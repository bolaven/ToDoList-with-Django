from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import*

# Create your views here.
def index(request):
	# return HttpResponse("my_to_do_appp first page")
	todos = Todo.objects.all()
	content = {'todos': todos}
	return render(request, 'my_to_do_app/index.html',content)

# render html 파일을 사용자에게 보여주려면 render 함수
# request가 user나 session 같은 중요한 값들 전달
# 사용자가 특정 url에 접근해서 index 함수를 실행할때 기본적으로 request 를 받아와 user나 session 값 참조 

def createTodo(request):
	user_input_str = request.POST['todoContent']
	new_todo = Todo(content = user_input_str)
	new_todo.save()
	return HttpResponseRedirect(reverse('index'))
	# return HttpResponse("Create Todo를 할거야! ->"+ user_input_str)

def doneTodo(request):
	done_todo_id = request.GET['todoNum']
	print("완료한 todo의 id", done_todo_id)
	todo = Todo.objects.get(id = done_todo_id)
	todo.delete()
	return HttpResponseRedirect(reverse('index'))