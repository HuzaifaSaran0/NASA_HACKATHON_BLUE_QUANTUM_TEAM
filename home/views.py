from django.shortcuts import render,  redirect
from django.http import JsonResponse  
from .models import *

import random

def home(request):
    context = {'catgories': Types.objects.all()}
    
    if request.GET.get('gfg'):
        return redirect(f"/quiz/?gfg={request.GET.get('gfg')}")
    
    return render(request, 'home.html', context)

def quiz(request):
    context = {'gfg': request.GET.get('gfg')}
    return render(request, 'quiz.html', context)



def get_quiz(request):
    try:
        # Fetching all questions
        question_objs = Question.objects.all()

        # Apply filtering based on "gfg" if present in the URL
        if request.GET.get('gfg'):
            question_objs = question_objs.filter(gfg__gfg_name__icontains=request.GET.get('gfg'))

        # Shuffle the questions and limit to 10
        question_objs = list(question_objs)
        random.shuffle(question_objs)
        question_objs = question_objs[:10]  # Limit to 10 questions

        # Build the JSON response
        data = []
        for question_obj in question_objs:
            data.append({
                "uid": str(question_obj.uid),
                "gfg": question_obj.gfg.gfg_name,
                "question": question_obj.question,
                "marks": question_obj.marks,
                "answer": question_obj.get_answers(),
            })

        payload = {'status': True, 'data': data}
        return JsonResponse(payload)
    except Exception as e:
        print(e)
        return JsonResponse({'status': False, 'error': str(e)}) 
