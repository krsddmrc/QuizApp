from django.contrib import admin
from .models import Answer, Question, Quiz, Category

admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Category)
