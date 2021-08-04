from django.contrib import admin
from .models import Role, StudyGroup, Person, Lesson

admin.site.register(Role)
admin.site.register(StudyGroup)
admin.site.register(Person)
admin.site.register(Lesson)

# Register your models here.
