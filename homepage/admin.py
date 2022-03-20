from django.contrib import admin
from .models import course
from .models import student
#from .models import coursegrade
# Register your models here.

admin.site.register(course)
admin.site.register(student)
#admin.site.register(coursegrade)