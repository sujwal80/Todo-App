from django.contrib import admin
from .models import task
#from .forms import task_form
# Register your models here.

#form = task_form(task)

admin.site.register(task)