from django.shortcuts import render, HttpResponseRedirect, reverse, get_list_or_404, get_object_or_404
from .forms import RegistrationForm
from django.contrib.auth.decorators import login_required
from .models import *

def index(request):
    return render(request, 'application/index.html')

def registration(request):
    if request.method == 'POST':
        user = User()
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user.username = form.cleaned_data['email']
            user.email = form.cleaned_data['email']
            user.set_password(form.cleaned_data['password'])
            user.save()
            student = Student(user=user)
            student.save()
            return HttpResponseRedirect(reverse('application:account'))
    else:
        form = RegistrationForm()
    return render(request, 'application/registration.html', {'form': form})

@login_required
def account(request):

    user = request.user

    done_modules = list(map(int, user.student.done_modules.split(', ')))

    context = {
        'topics': Topic.objects.order_by('id'),
        'modules': Module.objects.order_by('id'),
        'questions': Question.objects.order_by('id'),
        'done_modules': done_modules,
    }
    return render(request, 'application/account.html', context)

@login_required
def topic(request, id):
    context = {
        'informations': get_list_or_404(Information, topic=id),
        'questions': get_list_or_404(Question, topic=id),
        'topic': get_object_or_404(Topic, id=id),
    }

    return render(request, 'application/topic.html', context)

@login_required
def info(request, id):

    context = {
        'information': get_object_or_404(Information, id=id),
    }
    return render(request, 'application/info.html', context)

@login_required
def question(request, id):

    context = {
        'question': get_object_or_404(Question, id=id),
        'answers': get_list_or_404(Answer, question=id),
    }

    return render(request, 'application/question.html', context)

def act(request):
    if '_login' in request.POST:
        return HttpResponseRedirect(reverse('login'))
    elif '_register' in request.POST:
        return HttpResponseRedirect(reverse('application:registration'))
