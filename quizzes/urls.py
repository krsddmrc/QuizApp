from rest_framework import routers
from django.urls import path, include
from .views import CategoryView, QuestionView, AnswerView, QuizView

router=routers.DefaultRouter()
router.register("quiz", QuestionView)
router.register("category", CategoryView)
router.register("question", QuizView)
router.register("answer", AnswerView)

urlpatterns = [
    path('', include(router.urls)), 
]
