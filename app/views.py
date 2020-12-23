from django.shortcuts import render, redirect
from app.forms import StudentForm
from app.models import Student
from django.http import HttpResponse

# Create your views here.

def create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        form.save()
        return redirect('/')
    else:
        form = StudentForm()
    return render(request, "create.html", {'form' : form})

def show(request):
    student = Student.objects.all()
    return render(request, "show.html", {'student' : student})

def edit(request):
    if request.method == 'POST':
        sid = request.POST['sid']
        student = Student.objects.get(sid = sid)
        return render(request, "edit.html", {'student' : student})
    else:
        return render(request, "update.html")

def update(request, sid):
    student = Student.objects.get(sid = sid)
    form = StudentForm(request.POST, instance = student)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html', {'student' : student})

def delete(request):
    if request.method == 'POST':
        sid = request.POST['sid']
        student = Student.objects.get(sid = sid)
        student.delete()
        return redirect('/')
    else:
        return render(request, "delete.html")

