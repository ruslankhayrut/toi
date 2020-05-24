from django.db import models
from django.contrib.auth.models import User
from django.core.validators import int_list_validator
from ckeditor_uploader.fields import RichTextUploadingField

class Module(models.Model):
    name = models.CharField(verbose_name='Название', max_length=100)

    def __str__(self):
        return self.name

class Topic(models.Model):
    name = models.CharField(verbose_name='Название', max_length=100)
    module = models.ForeignKey(Module, on_delete=models.CASCADE, verbose_name='Раздел')

    def __str__(self):
        return self.name

class Information(models.Model):

    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, verbose_name='Тема')
    text = RichTextUploadingField()

    def __str__(self):
        return self.topic.name + ' ' + str(self.id)

class Recomendation(models.Model):
    grade = models.PositiveSmallIntegerField(verbose_name='Класс', null=True)
    topic = models.TextField(verbose_name='Тема', max_length='200')
    text = RichTextUploadingField()

    def __str__(self):
        return 'Класс: {}, Тема: {}'.format(self.grade, self.topic)

class Question(models.Model):
    text = models.TextField(verbose_name='Текст')
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, verbose_name='Тема')
    correct_answer = models.PositiveSmallIntegerField(verbose_name='Правильный ответ', blank=True, null=True)


    def __str__(self):
        return self.text


class Answer(models.Model):

    text = models.CharField(verbose_name='Текст', max_length=100, blank=True, null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='Вопрос')

    def __str__(self):
        return str(self.id) + ' ' + str(self.text)


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    done_modules = models.CharField(validators=[int_list_validator], max_length=300, null=True, blank=True)
    done_topics = models.CharField(validators=[int_list_validator], max_length=300, null=True, blank=True)
    done_questions = models.CharField(validators=[int_list_validator], max_length=300, null=True, blank=True)
    wrong_questions = models.CharField(validators=[int_list_validator], max_length=300, null=True, blank=True)

    def parse_to_list(self, string):
        return list(map(int, string.split(', '))) if string else []


    def __str__(self):
        return self.user.username
