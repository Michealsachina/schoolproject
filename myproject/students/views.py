# students/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Student
from .forms import StudentForm
from myproject.school.models import School
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


def student_list(request):
    students = Student.objects.select_related('school').all()
    return render(request, "students/student_list.html", {"students": students})

def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, "students/student_detail.html", {"student": student})

def student_edit(request, pk):
    student = get_object_or_404(Student, pk=pk)

    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            student = form.save(commit=False)
            student.school = student.school  # 🔑 keep existing school
            student.save()
            if request.headers.get("x-requested-with") == "XMLHttpRequest":
                return JsonResponse({
                    "success": True,
                    "id": student.id,
                    "student_name": student.student_name,
                    "dob": student.dob.strftime("%B %d, %Y"),
                    "student_class": student.student_class,
                    "grade": student.grade,
                    "email": student.email or "",
                })
            else:
                return redirect("student_list")
        else:
            if request.headers.get("x-requested-with") == "XMLHttpRequest":
                return JsonResponse({"success": False, "errors": form.errors}, status=400)

    return JsonResponse({"success": False, "error": "Only POST allowed"}, status=405)


def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        school_id = student.school.id   # remember the school before delete
        student_name = student.student_name
        student.delete()
        messages.success(request, f"❌ Student '{student_name}' deleted successfully.")
        
        # If `next` param exists → redirect back to school page
        next_url = request.POST.get("next")
        if next_url:
            return redirect(next_url)

        # Otherwise → go back to global student list
        return redirect("student_list")
    return render(request, "students/student_confirm_delete.html", {"student": student})


def student_update_photo(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST" and request.FILES.get('photo'):
        student.photo = request.FILES['photo']
        student.save()
    return redirect('student_detail', pk=student.pk)