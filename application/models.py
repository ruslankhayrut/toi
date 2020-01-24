from django.db import models

class Module(models.Model):
    name = models.CharField(verbose_name='Название', max_length=100)

    def __str__(self):
        return self.name

class Topic(models.Model):
    name = models.CharField(verbose_name='Название', max_length=100)
    module = models.ForeignKey(Module, on_delete=models.CASCADE, verbose_name='Раздел')

    def __str__(self):
        return self.name

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