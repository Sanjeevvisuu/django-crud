from django.shortcuts import render, redirect

# Create your views here.
from rest_app.models import *
from .forms import *
# Create your views here.
# pagination
from django.core.paginator import Paginator


def get(request):
    stu = students.objects.all()

    # paginator
    paginator = Paginator(stu, 10)  # 10 contents or datas

    # it get the current page number from user
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, "index.html", {"page_obj": page_obj})


def create(request):
    form = create_student()
    if request.method == "POST":
        form = create_student(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    return render(request, "create.html", {"form": form})


def delete(request, id):
    stu = students.objects.get(id=id)
    stu.delete()
    return redirect("index")


def update(request, id):
    stu = students.objects.get(id=id)
    if request.method == "POST":
        stu = create_student(request.POST, instance=stu)
        if stu.is_valid():
            stu.save()
            return redirect("index")

    return render(request, "update.html", {"stu": stu})
