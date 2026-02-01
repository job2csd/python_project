from django.contrib import admin

# Register your models here (all).
from .models import *

#For Sum Metho
from django.db.models import Sum

# To show in admin side add model here
admin.site.register(Receipe)
admin.site.register(StudentID)
admin.site.register(Department)
admin.site.register(Student)

#report card related
admin.site.register(Subject)

# Over right list display in admin side
#admin.site.register(SubjectMarks)
class SubjectMarkAdmin(admin.ModelAdmin):
    list_display=['student','subject','marks'] # type: ignore

admin.site.register(SubjectMarks,SubjectMarkAdmin)

#Student Report Card
class ReportCardAdmin(admin.ModelAdmin):
    list_display=['student','student_rank','total_marks','date_of_report_card_generation'] # type: ignore
    def total_marks(self,obj):
        subject_marks = SubjectMarks.objects.filter(student=obj.student)
        marks = subject_marks.aggregate(marks = Sum('marks'))
        return marks['marks']

admin.site.register(ReportCard,ReportCardAdmin)


