from django.shortcuts import render, redirect, HttpResponse
from models import * 
from django.contrib import messages

def index(request):
    response = "Courses"
    return HttpResponse(response)

def course(request):
    courses = Course.objects.all()
    data = {
        'courses':courses
    }
    return render(request, 'course/coursedash.html', data)
    # return render(request, 'course/coursedash.html', {'all_course':Course.objects.all()})

def create(request):
    if request.method == "POST":
        errors = Course.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for error in errors.itervalues():
                messages.error(request, error)
            return redirect('/course')
        else:
            Course.objects.create(name=request.POST['inputed_name'], desc=request.POST['inputed_desc'])
            return redirect('/course')

def remove(request, course_number):
    Course.objects.get(id=course_number).delete()
    return redirect('/course')

def destroy(request, course_number):
    return render(request, 'course/destroy.html', {'course':Course.objects.get(id=course_number)})