from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import StudentsInfo
from .forms import StudentForm

def index(request):
    return render(request, 'index.html', {
        'students': StudentsInfo.objects.all()
    })

def view_student(request, id):
    student = StudentsInfo.objects.get(pk=id)
    return HttpResponseRedirect(reverse('index'))

def add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
          form.save()
        return render(request, 'add.html', {
            'form': StudentForm(),
            'success': True
        })
    
    else:
        form = StudentForm()
        return render(request, 'add.html', {
            'form': StudentForm()
        })
    
def edit(request, id):
  if request.method == 'POST':
    student = StudentsInfo.objects.get(pk=id)
    form = StudentForm(request.POST, instance=student)
    if form.is_valid():
      form.save()
      return render(request, 'edit.html', {
        'form': form,
        'success': True
      })
  else:
    student = StudentsInfo.objects.get(pk=id)
    form = StudentForm(instance=student)
  return render(request, 'edit.html', {
    'form': form
  })


def delete(request, id):
  if request.method == 'POST':
    student = StudentsInfo.objects.get(pk=id)
    student.delete()
  return HttpResponseRedirect(reverse('index'))