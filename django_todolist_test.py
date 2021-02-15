# 최초 가져오기
git clone 경로


# 업로드 과정
git init #  원격 저장소에 올리려는 프로젝트의 최상위 폴더에서 진행

# git add <업로드하려는 파일명>
git add . # 전체 다 올리기  어떤걸 올리는지 알려주는 과정 

git commit -m "project init"   # 코멘트 달기


# git config --global user.email "bolaven1@korea.ac.kr"
# git config --global user.email "Taekjoo Lee"
# git remote add origin https://github.com/taekjoo/ToDoList-with-Django.git

# 실제 업로드
git push -u origin master



# 장고 프로젝트 개설
django-admin startproject todolist

# todolist 폴더가 또 생긴다ㅏ.

# app 구성

python manage.py startapp my_to_do_app


# todolist 폴더안에 
# settings.py 에서  내가 만든 app 추가해줌

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'my_to_do_app' # 내가 생성한 app 추가
]


# URL 설정, 서버실행
python manage.py runserver

# todolist 폴더안에 
# urls.py
from django.urls import path, include # include 추가

urlpatterns = [
	path('', include('my_to_do_app.urls')), #
    path('admin/', admin.site.urls),
]

# mytodoapp 폴더안에 urls.py 생성 

from django.urls import path
from . import views

urlpatterns = [
	path('', views.index)

]


# html 파일을 테ㅔㅁ플릿으로 사용
# 장고는 해당 앱에ㅔ서 templates 라는 폴더를 탐색하게됨, 그 폴더를 찾아 내부에 있는 html 파일ㅇ르 불러와 사용한다
# html 파일을 사용할때는 app 내부에 templates라는 폴더와 templates라는 폴더 내부에 app 이름과 동일한 폴더가 존재하고
그 안에 html 파일이 존재해야한다. 


# ToDoList > my_to_do_app > models.py

from django.db import models

# Create your models here.
class Todo(models.Model):
	content = models.CharField(max_length = 255)

# 장고에서 하나의 모델은 하나의 클래스로 나타낸다. Todo 라는 클래스 이름이 결국 모델의 이름
# 클래스 내부에 데이터의 이름과 데이터의 형태를 정의하면 된다.
# model은 적어준 모델을 바탕으로 동일한 테이블을 데이터베이스에 만들어 주어야 한다.

manage 파일이 있는 경로로 이동 

# migration이란 단순히 데이터베이스에 전해줄 초안, 설계도, 작업지시서와 비슷한 역할
python manage.py makemigrations


# 실제 테이블을 만드려면
python manage.py migrate

# 기본적으로 장고에서 제공하는 model들이 있기에, 기본제공 model들 또한 데이터베이스에 적용되어 만드러잊ㅁ


# 장고 프로젝트 데이터베이스에 접근해서 확인 
python manage.py dbshell

# 테이블이 어떤 정보를 가지는지
PRAGMA table_info(my_to_do_app_todo);

#
순서(단순num) | 이름 | 형태 | notnull여부(비어있어도 되는지 정보) | pk여부
0|id|integer|1||1
1|content|varchar(255)|1||0

select * from my_to_do_app_todo;



# html 화면에서 사용자가 텍스트를 입력하고 버튼을 눌렀을때 해당 텍스트가 서버에 전송되도록 수정


index.html 파일을 켜서 

                <form action="" method="POST">{% csrf_token %}

form 태그의 action, method

method에는 post, get 방식 2가지
post 방식을 사용할때는 {% csrf_token %} 적어줘야한다

action은 서버로 데이터를 전달할 때 어떤 url로 전달할 것인지
action에 적어 주는 경로로 데이터가 전달된다.

                <form action="./createTodo/" method="POST">{% csrf_token %}

button을 누르면, form 안에 있는 데이터가 createTodo라는 url로 전달된다.


404 에러 발생


# Todolist > my_to_do_app > urls.py 파일 수정 
# createtodo 라는 url에 대해서는 views 파일의 createtodo에서 처리해줘!
# views.py 에서 처리할 createTodo 함수를 만들어줘야함. 

from django.urls import path
from . import views

urlpatterns = [
	path('', views.index)
	path('createTodo/', views.createTodo) 

]
#
# input 태그 안에 name이 todocontent를 통해 사용자가 입력한 문자열이 있는 input 태그 문자열을 받아온다

< inputid = "todoContent" name = "todoContent" type = "text"
class ="form-control" placeholder="메모할 내용을 적어주세요" >

def createTodo(request):
	user_input_str = request.POST['todoContent']
	return HttpResponse("Create Todo를 할거야! ->"+ user_input_str)


# 남은과제 2가지,  사용자가 입력한 문자열을 db에 저장
# db에 저장된 내용을 보여주기

from .models import*
views.py 파일과 같은 위치에 있는 models.py 에서 모든것을 import 한다



models.py를 불러오고,   Todo 클래스에 content를 저장하고
new_todo에 변수를 저장
그리고 .save를 통해 db에 저장

def createTodo(request):
	user_input_str = request.POST['todoContent']
	new_todo = Todo(content = user_input_str)
	new_todo.save()
	return HttpResponse("Create Todo를 할거야! ->"+ user_input_str)



python manage.py dbshell

select *
from my_to_do_app_Todo;

# urls.py 파일에 name 값 추가
# 각 path로 매핑시켜줄대 url 대신 name을 이용해서 접근할수 있도록

urlpatterns = [
	path('', views.index, name ='index'),
	path('createTodo/', views.createTodo, name ='createTodo')

]

# view.py 파일에 HttpResponseRedirect,  reverse import 해주기

from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# reverse 함수를 통해 index라는 url 찾음
# 이는 url.py 에서 이름을 준 index 와 일치해야함
# HttpResponseRedirect 함수를 통해 해당 url로 이동


def createTodo(request):
	user_input_str = request.POST['todoContent']
	new_todo = Todo(content = user_input_str)
	new_todo.save()
	return HttpResponseRedirect(reverse('index'))
	# return HttpResponse("Create Todo를 할거야! ->"+ user_input_str)


# views.py 파일, todo 모델에 접근하고 objects 접근하고 all 함수를 통해 모든 데이터를 가져옴
# content라는 딕셔너리를 만들어서 todos 라는 key에 할당시킨후
# render 함수 마지막에 content 딕셔너리를 함께 전달해준다.

def index(request):
	# return HttpResponse("my_to_do_appp first page")
	todos = Todo.objects.all()
	content = {'todos'=todos}
	return render(request, 'my_to_do_app/index.html',content)

# index.html 에   {%%}로 묶어서 todo에  todos를 받게 한다.
{ %for todo in todos %}

# {{}} 사용자에게 직접 보여주는 값,  {% %} 사용자에게 직접 보여주지않고 반복문 사용
< li class ="list-group-item" > {{todo.content}} < / li >


# hidden type 사용자에게 보이지 않는 요소, id를 이용해서 삭제
< input type = "hidden" id = "todoNum" name = "todoNum" value = "{{todo.id}}" > < / input >



# for 반복문안에서 데이터의 개수와 동일하게 반복됨.
# hidden이라 안보이지만, value가 todo.id를 가지게 했다.


{ %for todo in todos %}
< form action = "" method = "GET" >
< div class ="input-group" name='todo1' >
< li class ="list-group-item" > {{todo.content}} < / li >
< input type = "hidden" id = "todoNum" name = "todoNum" value = "{{ todo.id }}" > < / input >
< span class ="input-group-addon" >
< button type = "submit"

class ="custom-btn btn btn-danger" > 완료 < / button >
< / span >
< / div >
< / form >
{ % endfor %}

# deleteTodo 입력
< form
action = "./deleteTodo/"
method = "GET" >

# urls.py에  deletetodo의 path 지정

path('deleteTodo/', views.doneTodo, name='deleteTodo')

# views.py에 dontodo 만들어줌

def doneTodo(request):
	done_todo_id = request.GET['todoNum']
	print("완료한 todo의 id", done_todo_id)
	return HttpResponseRedirect(reverse('index'))

# 받아온 id 값 을 todo에 넣고, todo 데이터 자체에서 delete 함수 호출해서 데이터 삭제

def doneTodo(request):
	done_todo_id = request.GET['todoNum']
	print("완료한 todo의 id", done_todo_id)
	todo = Todo.objects.get(id = done_todo_id)
	todo.delete()
	return HttpResponseRedirect(reverse('index'))