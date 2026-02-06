from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import School
from .forms import SchoolForm
from students.forms import StudentForm  # we'll create this
from students.models import Student

def school_list(request):
    schools = School.objects.all().order_by("school_name")
    return render(request, "school/school_list.html", {"schools": schools})

def school_detail(request, pk):
    school = get_object_or_404(School, id=pk)
    students = school.students.all()
    return render(request, 'school/school_detail.html', {
        'school': school,
        'students': students
    })

def add_student(request, school_id):
    school = get_object_or_404(School, id=school_id)
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES)  # supports photo
        if form.is_valid():
            student = form.save(commit=False)
            student.school = school
            student.save()
            messages.success(request, f"Student '{student.student_name}' added to {school.school_name}.")
            return redirect('school_detail', pk=school.id)
    else:
        # prefill school's id in the form's initial (photo handled by form)
        form = StudentForm(initial={'school': school.id})
    return render(request, 'school/add_student.html', {'school': school, 'form': form})

def add_school(request):
    if request.method == "POST":
        form = SchoolForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "School added successfully!")
            return redirect("school_list")
    return redirect("school_list")

def edit_school(request, pk):
    school = get_object_or_404(School, pk=pk)
    if request.method == "POST":
        form = SchoolForm(request.POST, instance=school)
        if form.is_valid():
            form.save()
            messages.success(request, "School updated successfully!")
    return redirect("school_list")

def delete_school(request, pk):
    school = get_object_or_404(School, id=pk)

    if school.students.exists():
        messages.error(request, "This school cannot be deleted because students are already assigned.")
        return redirect('school_list')

    if request.method == "POST":
        school.delete()
        messages.success(request, "School deleted successfully.")
        return redirect('school_list')

    return redirect('school_list')
