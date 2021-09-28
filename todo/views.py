from django.shortcuts import render,HttpResponse,redirect
from .models import Todo

# Create your views here.
def index(request):
    

    return render(request,"index.html")

def addTodo(request):
    if request.method == 'GET':
        return redirect("/")
    else:
        title = request.POST.get("title")
        newTodo = Todo(titel = title, completed = False)

        newTodo.save()
        return redirect("/")

