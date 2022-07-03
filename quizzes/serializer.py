from rest_framework import serializers
from .models import Category, Quiz, Question, Answer

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model:Quiz
        fields=(
            "id",
            "name",
            "questions",
            "slug",
        )
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=(
            "id",
            "quiz",
            "category_name"
        )

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Answer
        fields=(
            "id",
            "text"
        )

class QuestionSerializer(serializers.ModelSerializer):
    answers=AnswerSerializer(many=True)   
    class Meta:
        model=Question
        fields=(
            "id",
            "question_text",
            "difficulty", 
            "answers" 
        )       


