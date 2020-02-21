from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import *

admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Profile)
admin.site.register(Answers)
admin.site.register(ConnectionQuizQuestion)
