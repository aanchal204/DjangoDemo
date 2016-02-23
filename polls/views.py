from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,Http404
from .models import Question
from django.template import loader

def index(request):
    #return HttpResponse("Welcome to Polls Page!!")
    latest_question_list = Question.objects.order_by('-publication_date')[:5]   #top 5 questions
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    #output = '\n'.join([q.question for q in latest_question_list])
    #return HttpResponse(output)
    return HttpResponse(template.render(context,request))
    #or simply return render(request, 'polls/index.html',context)

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except(Question.DoesNotExist):
        raise Http404("Question does not exist!")
    context = {
        'question' : question,
    }
    template = loader.get_template('polls/detail.html')
    #return HttpResponse(template.render(context,request))
    return render(request,'polls/detail.html',context);

def results(request, question_id):
    return HttpResponse("Results of %s" %question_id);

def vote(request, question_id):
    return HttpResponse("Votes of %s"%question_id);