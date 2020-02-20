from django.db import models

# Create your models here.
# Create your models here.

from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    is_admin = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)


class Quiz(models.Model):
    quiz_created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz_name = models.TextField(max_length=500, blank=True)
    quiz_description = models.TextField(max_length=500, blank=True)
    quiz_created_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.quiz_name


class Question(models.Model):
    question_description = models.TextField(max_length=500, blank=True)
    question_created_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.question_description


class ConnectionQuizQuestion(models.Model):
    quiz_id = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)


class Answers(models.Model):
    connection_quiz_question_id = models.ForeignKey(ConnectionQuizQuestion, on_delete=models.CASCADE)
    profile_id = models.ForeignKey(User, on_delete=models.CASCADE)
    answer_description = models.TextField(max_length=500, blank=True)
    time_stamp = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.answer_description
