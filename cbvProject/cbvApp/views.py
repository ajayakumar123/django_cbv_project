from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from cbvApp.models import Student
from django.urls import reverse_lazy

# Create your views here.


class HelloWorldView(View):

    def get(self,request):
        return HttpResponse('<h1>Hello World</h1>')

class TemplateView(TemplateView):

    template_name='cbvApp/home.html'


class StudentListView(ListView):
    model=Student
    template_name='cbvApp/home.html'
    context_object_name='student_list'


class StudentDetailView(DetailView):
    model=Student
    template_name = 'cbvApp/detail.html'
    context_object_name='student'


class StudentCreateView(CreateView):
    model=Student
    template_name = 'cbvApp/create.html'
    fields=('roll_number','name','marks','grade','address')


class StudentUpdateView(UpdateView):
    model=Student
    template_name = 'cbvApp/create.html'
    fields=('roll_number','name','marks','grade','address')

class StudentDeleteView(DeleteView):
    model=Student
    template_name = 'cbvApp/delete.html'
    success_url = reverse_lazy('list_view')
