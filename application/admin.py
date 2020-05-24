from django.contrib import admin
from .models import *
# Register your models here.
class TopicInline(admin.TabularInline):
    model = Topic

class ModuleAdmin(admin.ModelAdmin):

    inlines = [
        TopicInline,
    ]

class QuestionInline(admin.TabularInline):
    model = Question

class TopicAdmin(admin.ModelAdmin):

    inlines = [
        QuestionInline,
    ]

class AnswerInline(admin.TabularInline):

    model = Answer

class QuestionAdmin(admin.ModelAdmin):

    inlines = [
        AnswerInline,
    ]


admin.site.register(Module, ModuleAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
admin.site.register(Student)
admin.site.register(Information)
admin.site.register(Recomendation)