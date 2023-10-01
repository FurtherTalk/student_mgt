from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View

from .models import Student
from .forms import StudentForm


# def index(request):
#     students = Student.objects.all()
#     if request.method == 'POST':
#         form = StudentForm(request.POST)
#         if form.is_valid():
#             cleaned_data = form.cleaned_data
#             student = Student()
#             student.name = cleaned_data['name']
#             student.sex = cleaned_data['sex']
#             student.email = cleaned_data['email']
#             student.profession = cleaned_data['profession']
#             student.qq = cleaned_data['qq']
#             student.phone = cleaned_data['phone']
#             student.save()
#             return HttpResponseRedirect(reverse('index'))
#             # return redirect('student:index')
#     else:
#         form = StudentForm()

#     context = {
#         'students': students,
#         'form': form
#     }
#     return render(request, 'index.html', context)


# def index(request):
#     students = Student.get_all()
#     if request.method == 'POST':
#         form = StudentForm(request.POST)
#         if form.is_valid():
#             form.save()
#             # return HttpResponseRedirect(reverse('index'))
#             return redirect('student:index')
#     else:
#         form = StudentForm()

#     context = {
#         'students': students,
#         'form': form
#     }
#     return render(request, 'index.html', context)

class IndexView(View):
    template_name = 'index.html'

    def get_context(self):
        students = Student.get_all()
        context = {
            'students': students, 
        }
        return context
    
    def get(self, request):
        context = self.get_context()
        form = StudentForm()
        context.update(
            {'form': form}
        )
        return render(request, self.template_name, context)
    
    def post(self, request):
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student:index')
        context = self.get_context()
        context.append(
            {'form': form}
        )
        return render(request, self.template_name, context)