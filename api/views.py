from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from .models import *

import datetime


def create_quiz(request):
    user = request.user

    print(user)

    return render(request, 'create_quiz.html', {'user': user})


@csrf_exempt
def create_quiz_api(request):
    if request.method == 'POST':

        user = request.user
        quiz = Quiz()

        quiz.quiz_name = request.POST['quiz_name']

        quiz.quiz_created_by = request.user
        quiz.quiz_description = "Qwerty"
        quiz.quiz_created_date = datetime.datetime.now()
        quiz.save()

        print("quiz has been saved")

        print(request.POST)

        print(user)

        return render(request, 'create_questions.html', {'quiz': quiz})
    else:
        pass
