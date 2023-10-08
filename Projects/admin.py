from django.contrib import admin
from .models import Course, Instructor, Lesson

class CourseAdmin(admin.ModelAdmin):
    fields = ['name', 'description']
admin.site.register(Course, CourseAdmin)
admin.site.register(Instructor)


class InstructorAdmin(admin.ModelAdmin):
    fields = ['user', 'full_time']
admin.site.register(Instructor, InstructorAdmin)

class LessonInline(admin.StackedInline):
    model= Lesson
    extra = 5

class CourseAdmin(admin.ModelAdmin):
    fields = ['name', 'description']
    inlines = [LessonInline]
admin.site.register(Course, CourseAdmin)