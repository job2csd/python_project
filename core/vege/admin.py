from django.contrib import admin

# Register your models here (all).
from .models import *

# To show in admin side add model here
admin.site.register(Receipe)
admin.site.register(StudentID)
admin.site.register(Department)
admin.site.register(Student)

