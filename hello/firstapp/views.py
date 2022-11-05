from .forms import UserForm
from django.shortcuts import render


def index(request):
    userform = UserForm()
    return render(request, "firstapp/index.html", {"form": userform})

     #if request.method == "POST":
        #name = request.POST.get("name")  # получить значение поля Имя
        #age = request.POST.get("age")  # получить значение поля Возраст
       # output = "<h2>Пользователь</h2><h3>Имя - {0}, Возраст - {1}</h3>".format(name, age)
       #return HttpResponse(output)
    #else:
       # userform = UserForm()
       #return render(request, "firstapp/index.html", {"form": userform})
