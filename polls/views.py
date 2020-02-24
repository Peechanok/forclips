import json

from django.contrib.auth import authenticate, login, logout
from django.db.models import Count
from django.forms import formset_factory
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render

from polls.models import Answer, Poll, Question

# Create your views here.
def my_login(request):
    context = {}

    return render(request, template_name='login.html', context=context)


def my_logout(request):
    logout(request)
    return redirect('login')


def index(request):
    search = request.GET.get('search', '')

    poll_list = Poll.objects.filter(
        del_flag=False, title__icontains=search
    ).annotate(question_count=Count('question')) # COUNT(*) GROUP BY

    context = {
        'poll_list': poll_list,
        'search': search
    }

    return render(request, template_name='polls/index.html', context=context)


def detail(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)

    return render(request, 'polls/detail.html', { 'poll': poll })


def create(request):
    return HttpResponse('This is create page!')
