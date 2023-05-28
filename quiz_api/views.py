from django.shortcuts import render

# Create your views here.

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Quiz
from .serializers import QuizSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404

@api_view(['POST'])
def create_quiz(request):
    serializer = QuizSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_active_quiz(request):
    active_quiz = Quiz.objects.filter(status='active')
    if active_quiz:
        serializer = QuizSerializer(active_quiz, many=True)
        return Response(serializer.data)
    return Response({'Msg': 'No active quiz found.'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_quiz_result(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    if quiz.status != 'finished':
        return Response({'detail': 'Quiz result not available yet.'}, status=status.HTTP_404_NOT_FOUND)
    return Response({'result': quiz.right_answer})

@api_view(['GET'])
def get_all_quiz(request):
    quizzes = Quiz.objects.all()
    serializer = QuizSerializer(quizzes, many=True)
    return Response(serializer.data)
