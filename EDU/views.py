from django.shortcuts import render
from EDU.models import *
import datetime
# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse


def add_members(request):
    d = datetime.date(2011, 10, 19)
    # member = Professor(firstname='Ali', lastname='Abam', staff_number='12', department=None, hiring_date=d, phone='1234')
    # course = Course(course_name='DS', offered_by=member, course_code='123_1', department=None, unit_count=3, semester='1234444')
    # student = Student(firstname='Ali', lastname='Sadeghi', student_number='400108858', enrollment_year='1400', major='CE', phone='1234')
    student = Student.objects.all()[0]
    course = Course.objects.all()[2]
    classroom = Classroom.objects.all()[1]
    # enrolment = Enrollment(student=student, course=course, semester='1234')
    # enrolment = Classroom(class_name='A12')
    enrolment = Schedule(classroom= classroom, course= course, time= '9-10:30')
    enrolment.save()

    return HttpResponse("Hello world!")