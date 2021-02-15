# ToDoList > my_to_do_app > models.py

from django.db import models

# Create your models here.
class Todo(models.Model):
	content = models.CharField(max_length = 255)

# 장고에서 하나의 모델은 하나의 클래스로 나타낸다. Todo 라는 클래스 이름이 결국 모델의 이름
# 클래스 내부에 데이터의 이름과 데이터의 형태를 정의하면 된다.
# model은 적어준 모델을 바탕으로 동일한 테이블을 데이터베이스에 만들어 주어야 한다.

