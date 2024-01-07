from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Student
from .forms import StudentForm
from django.template.loader import get_template
from xhtml2pdf import pisa
# Create your views here.

def homepage(request):
    students = Student.objects.all()
    return render(request, 'homepage.html', {'students': students})

# Create in CRUD
def add_student(request):
  if request.method == 'POST':
      form = StudentForm(request.POST, request.FILES)
      if form.is_valid():
          form.save()
          return redirect('homepage')
  else:
      form = StudentForm()
  return render(request, 'add_student.html', {'form': form})

# Read in CRUD
def read_student(request, matric_number):
  student = get_object_or_404(Student, matric_number= matric_number)
  return render(request, 'read_student.html', {'student': student})

def download_report(request, matric_number):
    student = get_object_or_404(Student, matric_number=matric_number)

    # Create a PDF report
    template_path = 'read_student.html'
    context = {'student': student}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{matric_number}_report.pdf"'

    template = get_template(template_path)
    html = template.render(context)

    # Create PDF
    pisa_status = pisa.CreatePDF(html, dest=response)

    # Return the response
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
  
# Update in CRUD
def edit_student(request, matric_number):
    student = get_object_or_404(Student, matric_number=matric_number)

    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = StudentForm(instance=student)

    return render(request, 'edit_student.html', {'form': form, 'student': student})
  
# Delete in CRUD
def delete_student(request, matric_number):
    student = get_object_or_404(Student, matric_number=matric_number)

    if request.method == 'POST':
        student.delete()
        return redirect('homepage')

    return render(request, 'delete_student.html', {'student': student})
