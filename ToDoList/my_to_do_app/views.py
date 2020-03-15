from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):
    todos = Todo.objects.all()
    content = {'todos': todos}
    return render(request, 'my_to_do_app/index.html', content)


def createTodo(request):
    user_input_str = request.POST['todoContent']
    new_todo = Todo(content = user_input_str)
    new_todo.save()
    return HttpResponseRedirect(reverse('index'))
    # return HttpResponse("create Todo를 할 거야! =>"+user_input_str)


def doneTodo(request):
    done_todo_id = request.GET['todoNum']
    print('완료한 todo의 id', done_todo_id)
    todo = Todo.objects.get(id= done_todo_id)
    todo.isDone = True
    todo.save()
    return HttpResponseRedirect(reverse('index'))


def deleteTodo(request):
    todo = Todo.objects.all()
    todo.delete()
    print('모든 메모가 삭제되었습니다.')
    return HttpResponseRedirect(reverse('index'))

