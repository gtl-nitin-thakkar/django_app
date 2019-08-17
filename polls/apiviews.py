from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Question
from .serializers import QuestionSerializer

@api_view(['GET', 'POST'])
def questions_view(request):
    if request.method == 'GET':
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            question = serializer.save()
            return Response(QuestionSerializer(question).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PATCH', 'DELETE'])
def question_detail_view(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'GET':
        serializer = QuestionSerializer(question)
        return Response(serializer.data)
    elif request.method == 'PATCH':
        raise NotImplementedError("PATCH currently not supported")
    elif request.method == 'DELETE':
        raise NotImplementedError("DELETE currently not supported")
