from django.contrib import admin
from cbvApp.models import Student
# Register your models here.

class StudentAdmin(admin.ModelAdmin):

    list_display = ['roll_number','name','marks','grade','address']


admin.site.register(Student,StudentAdmin)