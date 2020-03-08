import json

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.forms import formset_factory
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render

from polls.models import Answer, Poll, Question


# Create your views here.
def my_login(request):
    context = {}

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('index')
        else:
            context['username'] = username
            context['password'] = password
            context['error'] = 'Wrong username or password!'

    return render(request, template_name='login.html', context=context)


def my_logout(request):
    logout(request)
    return redirect('login')

@login_required
def change_password(request):
    context = {}
    if request.method == 'POST':
        user = request.user
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        # check that the passwords match
        if password1 == password2:
            user.set_password(password1)
            user.save()
            
            logout(request)
            return redirect('login')
        else:
            context['error'] = 'Passwords do not match.'

    return render(request, template_name='change_password.html', context=context)

@login_required
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


@login_required
def detail(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)

    return render(request, 'polls/detail.html', { 'poll': poll })
