from django.contrib import admin

from .models import Student, Teacher


class StudentTeacherInline(admin.TabularInline):
    model = Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    pass
    # list_display = ['id', 'name', 'group']
    # list_filter = ['group']


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    pass
    # list_display = ['id', 'name', 'subject', 'students']
    # list_filter = ['subject']
