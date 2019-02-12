from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from .models import Userdata, Question


# Create your views here.

def home(request):
    if(request.method == 'POST'):
        return redirect('/accounts/google/login')
    return render(request, 'index.html')


def loading(request):
    return render(request, 'loader.html')


def roulette(request):
    return render(request, 'roulette.html')


def l_out(request):
    logout(request)
    return redirect('/')


def quiz(request, filename):
    print("This function.")
    return render(request, filename)


def postanswer(request, filename):
    jsonobj = json.load(request.body.decode('utf-8'))
    question_no = jsonobj['question_no']
    question = Question.objects.filter(question_no=question_no)
    selected_choice = jsonobj['selected_choice']
    if question.question_no == question_no:
        if question.reality_type == 'MAGIC':
            if selected_choice == question.correct_choice:
                power = request.user.magicmarks
                request.user.score += 2 ** power
                request.user.magicmarks += 1
            else:
                request.user.magicmarks = 0
        elif question.reality_type == 'ROBOTICS':
            if selected_choice == question.correct_choice:
                simcorrect = request.user.roboticsmarks
                if simcorrect < 5:
                    request.user.roboticsmarks += 1
                else:
                    request.user.score += 25
            else:
                request.user.roboticsmarks = 0
        elif question.reality_type == 'GAMING':
            if selected_choice == question.correct_choice:
                request.user.score += 4
            else:
                request.user.score -= 1
        elif question.reality_type == 'MYTHOLOGY':
            if selected_choice == question.correct_choice:
                correct = request.user.mythologymarks
                if correct == 1:
                    request.user.score += 2
                elif correct == 2:
                    request.user.score += 3
                elif correct == 3:
                    request.user.score += 5
                elif correct == 4:
                    request.user.score += 8
                elif correct == 5:
                    request.user.score += 13
                correct += 1
    return HttpResponse('')


# 1. powerscheme - 2 ki power, resets on wrong answer
# 2. all or nothing - all sahi to number warna gaye
# 3. normal marking with negative +4 -1
# 4. fibonacci marking
# json.load(request.body.decode('utf-8'))
# index
# questions send
# answer check
# leaderboard
# score calculate
# reality check
# total score
