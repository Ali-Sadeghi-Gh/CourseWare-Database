from django.shortcuts import render
from EDU.models import *
import datetime
# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse


def add_members(request):
    d = datetime.date(2011, 10, 19)
    member = Professor(firstname='Ali', lastname='Abam', staff_number='12', department=None, hiring_date=d, phone='1234')
    department = Department(name='CE', head_of_department = member)
    member.save()
    department.save()

    return HttpResponse("Hello world!")