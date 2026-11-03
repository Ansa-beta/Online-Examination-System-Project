from django.db import models

# Create your models here.
class QuestionDb(models.Model):
    question=models.CharField(max_length=100)
    option_a=models.CharField(max_length=100)
    option_b=models.CharField(max_length=100)
    option_c=models.CharField(max_length=100)
    option_d=models.CharField(max_length=100)
    correct_answer = models.CharField(max_length=1, choices=[
        ('A', 'Option A'),
        ('B', 'Option B'),
        ('C', 'Option C'),
        ('D', 'Option D')
    ])
    def __str__(self):
        return self.question

class SubmissionDb(models.Model):
    question_id = models.IntegerField()
    student_name = models.CharField(max_length=100)
    selected_answer = models.CharField(max_length=1, choices=[
        ('A', 'Option A'),
        ('B', 'Option B'),
        ('C', 'Option C'),
        ('D', 'Option D')
    ])
    is_correct = models.BooleanField(default=False)
    obtained_marks = models.IntegerField(default=0)

    def __str__(self):
        return self.student_name


    