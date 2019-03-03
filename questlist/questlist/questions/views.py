from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.urls import reverse

from .models import Question


def index(request):
    list = Question.objects.all()
    return render(request, 'questions/index.html', {'list': list})

def add(request):
    try:
        text = request.POST['text']
    except KeyError:
        return render(request, 'questions/index.html', {
            'error_message': "Поле текста пустое",
            'list': []
        })
    else:
        question = Question()
        question.text = text
        question.save()
        return HttpResponseRedirect(reverse('questions:index'))