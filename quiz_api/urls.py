from quiz_api import views
from django.urls import path

urlpatterns = [
    path('quizzes', views.create_quiz, name="Creat_Quiz"),
    path('quizzes/active', views.get_active_quiz, name="active_quiz"),
    path('quizzes/<int:quiz_id>/result', views.get_quiz_result, name="quiz_result"),
    path('quizzes/all', views.get_all_quiz, name="all_results"),
]