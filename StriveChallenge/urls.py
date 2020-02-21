"""StriveChallenge URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from api.views import create_quiz, create_quiz_api, create_questions_api, home, indi_quiz, submit_answer_api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create_quiz/', create_quiz),
    path('create_quiz_api/', create_quiz_api, name="create_quiz_api"),
    path('create_questions_api/', create_questions_api, name="create_questions_api"),
    path('home/', home),
    path('home/<int:quiz_id>/', indi_quiz, name='indi_quiz'),
    # path('home/<int:quiz_id>/', indi_question, name='indi_question'),
    path('submit_answer_api/', submit_answer_api, name='submit_answer_api'),

]
