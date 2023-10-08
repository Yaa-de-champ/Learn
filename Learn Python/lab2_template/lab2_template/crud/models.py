from django.db import models
from django.utils.timezone import now

# Define your models from here:
class User(models.Model):
    first_name = models.CharField(null=False, max_length=30, default='Nana Yaa')
    last_name = models.CharField(null=False, max_length=30, default='Doku-Amponsah')
    dob = models.DateField(null=True)
    email = models.EmailField(null=False, unique=True)
    location = models.CharField(null=True, max_length=225)

    def __str__(self):
        return self.first_name + " " + self.last_name

# an instructor model inherited from the user model

class Instructor(User):
    full_time = models.BooleanField(default=True)
    total_learners = models.IntegerField()

    def __str__(self):
        return "First name: " + self.first_name + ", " + \
                "Last name: " + self.last_name + ", " + \
                "Is full time: " + str(self.full_time) + ", " + \
                "Total learners: "+ str(self.total_learners) + ", "
    
# course model which has a many to many relationship to instructor model
class Course(models.Model):
    name = models.CharField(null=False, max_length=100, default='Online course')
    description = models.CharField(max_length=500)
    # many to many relationship
    instructors = models.ManyToManyField(Instructor)

    def __str__(self):
        return "Name: " + self.name + ", " + \
        "Description: "  + self.description
    

# course model which has a one to many relationship to a lesson model
class Lesson(models.Model):
    title = models.CharField(max_length=200, default="Title")
    course = models.ForeignKey(Course, null=True, on_delete=models.CASCADE)
    content = models.TextField()


class Learner(User):
    STUDENT = 'student'
    DEVELOPER = 'developer'
    DATA_SCIENTIST = 'data_scientist'
    DATABASE_ADMIN = 'dba'
    OCCUPATION_CHOICES = [
        (STUDENT, 'Student'),
        (DEVELOPER, 'Developer'),
        (DATA_SCIENTIST, 'Data Scientist'),
        (DATABASE_ADMIN, 'Database Admin')
    ]

# Occupation Char field with defined enumeration choices
    occupation = models.CharField(
        null=False,
        max_length=20,
        choices=OCCUPATION_CHOICES,
        default=STUDENT
    )
    # Social link URL field
    social_link = models.URLField(max_length=200)
    
    # Create a toString method for object string representation
    def __str__(self):
        return "First name: " + self.first_name + ", " + \
                "Last name: " + self.last_name + ", " \
                "Date of Birth: " + str(self.dob) + ", " + \
                "Occupation: " + self.occupation + ", " + \
                "Social Link: " + self.social_link
    

class Enrollment(models.Model):
    AUDIT = 'audit'
    HONOR = 'honor'
    COURSE_MODES = [
        (AUDIT, 'Audit')
        (HONOR, 'Honors')
    ]

    learner = models.ForeignKey(Learner, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_enrolled = models.DateField(default=now)
    mode = models.CharField(max_length=5, choices=COURSE_MODES, default=AUDIT)

class Course(models.Model):
    name = models.CharField(null=False, max_length=100, default='online course')
    description = models.CharField(max_length=500)
    instructors = models.ManyToManyField(Instructor)
    learners = models.ManyToManyField(Learner, through='Enrollment')

    def __str__(self):
        return "Name: " + self.name + ", " + \
        "Description: " + self.description
    def __str__(self):
        return "Name: " + self.name + ", " + \
        "Description: " + self.description