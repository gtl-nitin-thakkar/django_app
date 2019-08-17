from rest_framework import serializers
from .models import Question

class QuestionSerializer(serializers.Serializer):
    question_text = serializers.CharField(max_length=200)
    pub_date = serializers.DateTimeField()
	
	was_published_recently = serializers.BooleanField(read_only=True)
    verbose_question_text = serializers.CharField(read_only=True)

    # DRF serializer.save() calls self.create(self.validated_data)
    def create(self, validated_data):
        return Question.objects.create(**validated_data)

