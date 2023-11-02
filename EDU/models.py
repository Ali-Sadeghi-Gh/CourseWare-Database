from django.db import models


class Student(models.Model):

    MAJOR_CHOICES = [
        ("CE", "Computer Engineering"),
        ("CS", "Computer Science"),
        ("EE", "Electrical Engineering"),
        ("Ph", "Physics")
    ]

    firstname = models.CharField(max_length=255, blank=False)
    lastname = models.CharField(max_length=255, blank=False)
    student_number = models.IntegerField(max_length=9, primary_key=True, unique=True, blank=False)
    phone = models.CharField(max_length=11)
    enrollment_year = models.CharField(max_length=4, default=None, blank=False)
    major = models.CharField(max_length=4, choices=MAJOR_CHOICES, blank=False)

    def __str__(self):
        return "firstname: " + self.firstname + "\nlastname: " + self.lastname + "\nstudent number: " + str(self.student_number)


class Professor(models.Model):

    firstname = models.CharField(max_length=255, blank=False)
    lastname = models.CharField(max_length=255, blank=False)
    staff_number = models.IntegerField(max_length=5, primary_key=True, unique=True, blank=False)
    phone = models.CharField(max_length=11)
    hiring_date = models.DateField(blank=False)
    department = models.ForeignKey('Department', blank=False, on_delete=models.SET_NULL, null=True, related_name='+')

    def __str__(self):
        return "firstname: " + self.firstname + "\nlastname: " + self.lastname + "\nstaff number: " + str(self.staff_number)


class Course(models.Model):

    course_name = models.CharField(max_length=255, blank=False)
    course_code = models.CharField(max_length=9, blank=False)
    unit_count = models.IntegerField(max_length=1)
    offered_by = models.ForeignKey(Professor, blank=False, on_delete=models.SET_NULL, null=True)
    semester = models.CharField(max_length=6, blank=False)
    department = models.ForeignKey('Department', default=None, on_delete=models.SET_NULL, null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['course_code', 'semester'], name='course_keys_combination'
            )
        ]

    def __str__(self):
        return "course name: " + self.course_name + "\ncourse code: " + str(self.course_code)


class Enrollment(models.Model):

    student = models.ForeignKey(Student, blank=False, on_delete=models.SET_NULL, null=True)
    course = models.ForeignKey(Course, blank=False, on_delete=models.SET_NULL, null=True)
    semester = models.CharField(max_length=6, blank=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['student', 'course', 'semester'], name='enrollment_keys_combination'
            )
        ]


class Department(models.Model):

    DEPARTMENT_CHOICES = [
        ("CE", "Computer Engineering"),
        ("CS", "Computer Science"),
        ("EE", "Electrical Engineering"),
        ("Ph", "Physics")
    ]

    name = models.CharField(max_length=4, choices=DEPARTMENT_CHOICES)
    head_of_department = models.ForeignKey(Professor, default=None, on_delete=models.SET_NULL, null=True, related_name='+')

    def __str__(self):
        name = None if self.head_of_department is None else self.head_of_department.lastname
        return "name: " + self.name + "\nhead_of_department: " + name


class Classroom(models.Model):

    class_name = models.CharField(max_length=255, primary_key=True, blank=False)
    class_capacity = models.IntegerField(null=True, default=0)

    def __str__(self):
        return "class name: " + self.class_name + " class capacity: " + str(self.class_capacity)


class Schedule(models.Model):

    course = models.ForeignKey(Course, blank=False, on_delete=models.SET_NULL, null=True)
    classroom = models.ForeignKey(Classroom, blank=False, on_delete=models.SET_NULL, null=True)
    time = models.CharField(max_length=10, blank=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['course', 'classroom', 'time'], name='schedule_keys_combination'
            )
        ]

