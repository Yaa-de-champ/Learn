# Django specific settings
import inspect
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
from django.db import connection
# Ensure settings are read
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from crud.models import *
from datetime import date


# Your code starts from here:
def write_instructors():
    # add instructors
    # create a user
    user_yaa = User(first_name='Nana Yaa', last_name='Doku-Amponsah', dob=date(1962, 7, 16))
    user_yaa.save()
    instructor_yaa = Instructor(full_time=True, total_learners=30050)
    # update the user reference of instructor_yaa to be user_yaa
    instructor_yaa.user = user_yaa
    instructor_yaa.save()

    instructor_kwame = Instructor(first_name='kwame', last_name='Doku-Amponsah', dob=date(1987, 7, 19))
    instructor_kwame.save()

    instructor_kobby = Instructor(first_name='kobby', last_name='Doku-Amponsah', dob=date(1998, 6, 17))
    instructor_kobby.save()

    print('Instructor objects all saved.....')


def write_courses():
    # Add Courses
    course_cloud_app = Course(name="Cloud Application Development with Database",
                                description="Develop and deploy application on cloud")
    course_cloud_app.save()
    course_python = Course(name="Introduction to Python",
                            description="Learn core concepts of Python and obtain hands-on "
                                        "experience via a capstone project")
    course_python.save()

    print("Course objects all saved... ")


def write_lessons():
    # Add lessons
    lession1 = Lesson(title='Lesson 1', content="Object-relational mapping project")
    lession1.save()
    lession2 = Lesson(title='Lesson 2', content="Django full stack project")
    lession2.save()
    print("Lesson objects all saved... ")


def clean_data():
    # Delete all data to start from fresh
    Enrollment.objects.all().delete()
    User.objects.all().delete()
    Learner.objects.all().delete()
    Instructor.objects.all().delete()
    Course.objects.all().delete()
    Lesson.objects.all().delete()


# Clean any existing data first
clean_data()
write_courses()
write_instructors()
write_lessons()