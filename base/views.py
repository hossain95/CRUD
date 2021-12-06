from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .models import StudentInfo
from .forms import StudentForm

# Create your views here.
students = [
    {
        "id": 1,
        "name": "Mia Hossain",
        "age": 25
    },
    {
        "id": 2,
        "name": "Roma Akter",
        "age": 24
    },
    {
        "id": 3,
        "name": "Sabina Akter",
        "age": 18
    },
    {
        "id": 4,
        "name": "Lima Akter",
        "age": 17
    }
]


def home(request):
    context = {"students": students}
    return render(request, 'home.html', context)


def detail(request, pk):
    st = None
    for student in students:
        if student["id"] == int(pk):
            st = student
    context = {"student": st}
    return render(request, 'details.html', context)


def create_view(request):
    context = {}
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {'form': form}
    return render(request, "create_view.html", context)


def list_view(request):
    students = StudentInfo.objects.all()
    context = {"students": students}
    return render(request, 'list_view.html', context)


def details_view(request, id):
    student = StudentInfo.objects.get(id=id)
    context = {"student": student}
    return render(request, "detail_view.html", context)

def update_view(request, id):
    context = {}
    obj = get_object_or_404(StudentInfo, id=id)
    form = StudentInfo(request.POST, instance = obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/"+id)
    context = {"form": form}
    return render(request, "update_view.html", context)