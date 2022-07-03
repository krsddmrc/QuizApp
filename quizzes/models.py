from django.db import models
from django.contrib.auth.models import User

class Answer(models.Model):
    text = models.CharField(max_length=128, verbose_name=u'Answer\'s text')
    is_valid = models.BooleanField(default=False)

    def __str__(self):
        return self.text


class Question(models.Model):
    DEGREES = (
        ('E', 'EASY'),
        ('M', 'MIDDLE'),
        ('H', 'HARD'),
        ('VH', 'VERYHARD'),
        )
    question_text = models.CharField(max_length=256, verbose_name=u'Question\'s text')
    answers = models.ManyToManyField(Answer)
    is_published = models.BooleanField(default=False,)
    difficulty=models.CharField(max_length=2, choices=DEGREES)

    def __str__(self):
        return "{content} - {published}".format(content=self.question_text, published=self.is_published)

class Quiz(models.Model):
   
    name = models.CharField(max_length=64, verbose_name=u'Quiz name', )
    slug = models.SlugField(max_length=64, verbose_name=u'Category', )
    questions = models.ManyToManyField(Question)

  
    def __str__(self):
        return f'{self.name} - {self.slug}'


class Category(models.Model):
    category_name = "slug"
    quiz = models.ManyToManyField(Quiz,)
  
    def __str__(self):
        return f'{self.category_name}'
        