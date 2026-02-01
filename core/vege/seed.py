from faker import Faker
import random
from .models import *

from django.db.models import Q,Sum # type: ignore

fake = Faker()

def seed_db(n=10)->None:
    try:
        for i in range(0,n):
            department_objs = Department.objects.all()
            department_index= random.randint(0,len(department_objs)-1)
            department      = department_objs[department_index]

            department = department
            student_id = f'STU-0{random.randint(100,999)}'
            student_name = fake.name()
            student_email = fake.email()
            student_age = random.randint(20,35)
            student_address = fake.address()

            student_id_obj = StudentID.objects.create(student_id=student_id)
            student_obj = Student.objects.create(
                department 		=department,
                student_id 		=student_id_obj,
                student_name 	=student_name,
                student_email 	=student_email,
                student_age 	=student_age,
                student_address =student_address
            )
    except Exception as e:
        print("Err===>",e)

def create_subject_marks(n):
    try:
        student_obj = Student.objects.all()
        for student in student_obj:
            subjects = Subject.objects.all()
            for subject in subjects:
                SubjectMarks.objects.create(
                    subject = subject,
                    student = student,
                    marks = random.randint(0,100)
                )

    except Exception as e:
        print("Err===>",e)

#Generate Ranks
def generate_report_card():
    print("CALLED")

    ranks = (
        Student.objects
        .annotate(total_marks=Sum('studentmarks__marks'))
        .order_by('-total_marks', '-student_age')
    )

    i = 1
    for student in ranks:
        ReportCard.objects.update_or_create(
            student_rank=i,
            defaults={
                'student': student
            }
        )
        i += 1