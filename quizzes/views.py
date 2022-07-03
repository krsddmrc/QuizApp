from django.shortcuts import render
from .serializer import  QuestionSerializer, CategorySerializer, QuizSerializer, AnswerSerializer
from .models import *
from rest_framework import viewsets
from .permission import IsStafforReadOnly

class QuestionView(viewsets.ModelViewSet):
    queryset=Question.objects.all()
    serializer_class=QuestionSerializer
    permission_classes=(IsStafforReadOnly,)

class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class QuizView(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer   
    
class AnswerView(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer