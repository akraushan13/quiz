from quiz_api import views
from django.urls import path

urlpatterns = [
    path('quiz', views.create_quiz, name="Creat_Quiz"),
    path('quiz/active', views.get_active_quiz, name="active_quiz"),
    path('quiz/<int:quiz_id>/result', views.get_quiz_result, name="quiz_result"),
    path('quiz/all', views.get_all_quiz, name="all_results"),
]