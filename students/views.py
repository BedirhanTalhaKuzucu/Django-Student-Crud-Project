from multiprocessing import context
from .forms import StudentForm
from django.shortcuts import render, redirect
from .models import Students
from django.contrib import messages


def student_add_update(request, id=0):
    if id:
        student = Students.objects.get(id=id)
        form = StudentForm(instance=student)

        if request.method == "POST":
            form = StudentForm(request.POST, instance=student)

            if form.is_valid():
                form.save()
                messages.success(request, "Student updated successful")
                return redirect("list")
    
        context= {
            "student" : student,
            "form" : form, 
        }
    else:
        form = StudentForm()
        if request.method == "POST":
            form = StudentForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Student added successful")
                return redirect("list")
        
        context = {
            "form" : form
        }
        
    return render(request, "students/student_form.html", context)


def student_list(request):
    students = Students.objects.all()
    context = {
        "students" : students
    }
    return render (request, "students/student_list.html", context )
    

def student_delete(request, id):
    student = Students.objects.get(id=id)

    if request.method == "POST":
        student.delete()
        messages.error(request, "Student deleted successful")
        return redirect('list')

    
    return render (request, "students/student_list.html")


