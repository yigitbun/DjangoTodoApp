from django.shortcuts import render,HttpResponse,redirect
from .models import Todo

# Create your views here.
def index(request):
    todos = Todo.objects.all()

    return render(request,"index.html", {"todos":todos})

def addTodo(request):
    if request.method == 'GET':
        return redirect("/")
    else:
        title = request.POST.get("title")
        newTodo = Todo(titel = title, completed = False)

        newTodo.save()
        return redirect("/")

