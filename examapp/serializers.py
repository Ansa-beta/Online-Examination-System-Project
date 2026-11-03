from rest_framework import serializers
from examapp.models import QuestionDb   #We do not need models here, because there is no choices in this project

class QuestionSerializer(serializers.Serializer):
    question=serializers.CharField(max_length=100)
    option_a=serializers.CharField(max_length=100)
    option_b=serializers.CharField(max_length=100)
    option_c=serializers.CharField(max_length=100)
    option_d=serializers.CharField(max_length=100)
    correct_answer = serializers.ChoiceField(choices=['A', 'B', 'C', 'D'])

class SubmissionSerializer(serializers.Serializer):
    question_id = serializers.IntegerField()
    student_name = serializers.CharField(max_length=100)
    selected_answer = serializers.ChoiceField(choices=['A', 'B', 'C', 'D'])
    is_correct = serializers.BooleanField(default=False)
    obtained_marks = serializers.IntegerField(default=0)
    
    def validate(self, validated_data):
        question_id=validated_data.get("question_id")
        if not QuestionDb.objects.filter(id=question_id).exists():
            raise serializers.ValidationError("Question does not exist")
        return validated_data
        