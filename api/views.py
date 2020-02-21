from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from .models import *

import json

import datetime
from django.http import HttpResponse

from .forms import MyForm


def create_quiz(request):
    user = request.user

    print(user)

    return render(request, 'create_quiz.html', {'user': user})


@csrf_exempt
def home(request):
    user = request.user

    quiz = Quiz.objects.all()

    print(user)

    return render(request, 'home.html', {'quiz': quiz})


@csrf_exempt
def indi_quiz(request, quiz_id):
    user = request.user

    quiz = Quiz.objects.get(id=quiz_id)

    conn = ConnectionQuizQuestion.objects.filter(quiz_id=quiz)

    ques = Question.objects.all()

    questions_list = []

    for c in conn:
        questions_list.append(ques.get(id=c.question_id.id))

    print(questions_list)

    print(user)

    return render(request, 'indi_question.html', {'quiz': quiz, 'questions': questions_list, 'con': conn})


@csrf_exempt
def submit_answer_api(request):
    user = request.user
    print(request.POST)

    quiz = Quiz.objects.get(id=request.POST['quiz_id'])

    con = ConnectionQuizQuestion.objects.filter(quiz_id=request.POST['quiz_id'])

    question_list = []

    for c in con:
        question_list.append(c.question_id)

    answer1 = Answers()
    connection1 = ConnectionQuizQuestion.objects.get(quiz_id=request.POST['quiz_id'],
                                                     question_id=question_list[0])
    answer1.answer_description = request.POST['answer_name'][0]
    answer1.connection_quiz_question_id = connection1
    answer1.profile_id = user
    answer1.time_stamp = datetime.datetime.now()
    answer1.save()

    answer2 = Answers()
    connection2 = ConnectionQuizQuestion.objects.get(quiz_id=request.POST['quiz_id'],
                                                     question_id=question_list[1])
    answer2.answer_description = request.POST['answer_name'][1]
    answer2.connection_quiz_question_id = connection2
    answer2.profile_id = user
    answer2.time_stamp = datetime.datetime.now()
    answer2.save()

    answer3 = Answers()
    connection3 = ConnectionQuizQuestion.objects.get(quiz_id=request.POST['quiz_id'],
                                                     question_id=question_list[2])
    answer3.answer_description = request.POST['answer_name'][2]
    answer3.connection_quiz_question_id = connection3
    answer3.profile_id = user
    answer3.time_stamp = datetime.datetime.now()
    answer3.save()

    answer4 = Answers()
    connection4 = ConnectionQuizQuestion.objects.get(quiz_id=request.POST['quiz_id'],
                                                     question_id=question_list[3])
    answer4.answer_description = request.POST['answer_name'][3]
    answer4.connection_quiz_question_id = connection4
    answer4.profile_id = user
    answer4.time_stamp = datetime.datetime.now()
    answer4.save()

    answer5 = Answers()
    connection5 = ConnectionQuizQuestion.objects.get(quiz_id=request.POST['quiz_id'],
                                                     question_id=question_list[4])
    answer5.answer_description = request.POST['answer_name'][4]
    answer5.connection_quiz_question_id = connection5
    answer5.profile_id = user
    answer5.time_stamp = datetime.datetime.now()
    answer5.save()

    return HttpResponse(
        json.dumps(
            {
                'sucess_message': "The answers have been saved"
            }
        ))


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

        return render(request, 'create_questions.html', {'quiz': quiz, })
    else:
        pass


@csrf_exempt
def create_questions_api(request):
    if request.method == 'POST':
        user = request.user

        print("quiz has been saved")

        print(request.POST)

        print(user)

        quiz = Quiz.objects.get(id=request.POST['quiz_id'])

        question1 = Question()
        question1.question_description = request.POST['ques_name_1']
        question1.question_created_date = datetime.datetime.now()
        question1.save()

        connection1 = ConnectionQuizQuestion()
        connection1.quiz_id = quiz
        connection1.question_id = question1
        connection1.save()

        question2 = Question()
        question2.question_description = request.POST['ques_name_2']
        question2.question_created_date = datetime.datetime.now()
        question2.save()

        connection2 = ConnectionQuizQuestion()
        connection2.quiz_id = quiz
        connection2.question_id = question2
        connection2.save()

        question3 = Question()
        question3.question_description = request.POST['ques_name_3']
        question3.question_created_date = datetime.datetime.now()
        question3.save()

        connection3 = ConnectionQuizQuestion()
        connection3.quiz_id = quiz
        connection3.question_id = question3
        connection3.save()

        question4 = Question()
        question4.question_description = request.POST['ques_name_4']
        question4.question_created_date = datetime.datetime.now()
        question4.save()

        connection4 = ConnectionQuizQuestion()
        connection4.quiz_id = quiz
        connection4.question_id = question4
        connection4.save()

        question5 = Question()
        question5.question_description = request.POST['ques_name_1']
        question5.question_created_date = datetime.datetime.now()
        question5.save()

        connection5 = ConnectionQuizQuestion()
        connection5.quiz_id = quiz
        connection5.question_id = question5
        connection5.save()

        return HttpResponse(
            json.dumps(
                {
                    'sucess_message': "The Questions have been created"
                }
            ))
    else:
        pass
