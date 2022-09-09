from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.http import HttpResponse
from .models import Course


def index(request, template_name='courses.html'):
    courses = Course.objects.order_by('id')
    context = {'courses': courses}
    return render(request, template_name, context)


class course(DetailView):
    model = Course
    locals()
    template_name = 'course.html'
