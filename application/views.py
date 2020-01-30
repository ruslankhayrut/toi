from django.shortcuts import render, HttpResponseRedirect, reverse, get_list_or_404, get_object_or_404, HttpResponse
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

    done_modules = parse_to_list(user.student.done_modules)

    context = {
        'topics': Topic.objects.order_by('id'),
        'modules': Module.objects.order_by('id'),
        'questions': Question.objects.order_by('id'),
        'done_modules': done_modules,
    }
    return render(request, 'application/account.html', context)

@login_required
def info(request, topic_id, info_id):
    user = request.user

    done_modules = parse_to_list(user.student.done_modules)
    done_topics = parse_to_list(user.student.done_topics)
    done_questions = parse_to_list(user.student.done_questions)
    wrong_questions = parse_to_list(user.student.wrong_questions)

    all_info = get_list_or_404(Information, topic=topic_id)
    if not info_id:
        info_id = all_info[0].id
        return HttpResponseRedirect(reverse('application:info', args=[topic_id, info_id]))
    else:
        info = get_object_or_404(Information, id=info_id)


    if request.method == "GET":
        context = {
            'informations': all_info,
            'req_information': info,
            'questions': get_list_or_404(Question, topic=topic_id),
            'req_topic': get_object_or_404(Topic, id=topic_id),
            'modules': Module.objects.order_by('id'),
            'topics': Topic.objects.order_by('id'),
            'done_modules': done_modules,
            'done_topics': done_topics,
            'done_questions': done_questions,
            'wrong_questions': wrong_questions,
        }
        return render(request, 'application/info.html', context)

@login_required
def question(request, topic_id, question_id):

    user = request.user
    done_questions = parse_to_list(user.student.done_questions)
    wrong_questions = parse_to_list(user.student.wrong_questions)
    done_modules = parse_to_list(user.student.done_modules)
    done_topics = parse_to_list(user.student.done_topics)

    if request.method == 'POST':

        question = Question.objects.get(id=question_id)

        if question.correct_answer == int(request.POST['answer']):
            done_questions.append(question_id)
            try:
                wrong_questions.remove(question_id)
            except ValueError:
                pass

            user.student.done_questions = ', '.join(str(n) for n in done_questions)
            user.student.wrong_questions = ', '.join(str(n) for n in wrong_questions)
            user.student.save()
        else:
            if question_id not in wrong_questions:
                wrong_questions.append(question_id)
                user.student.wrong_questions = ', '.join(str(n) for n in wrong_questions)
                user.student.save()



    context = {
        'informations': get_list_or_404(Information, topic=topic_id),
        'req_question': get_object_or_404(Question, id=question_id),
        'answers': get_list_or_404(Answer, question=question_id),
        'questions': get_list_or_404(Question, topic=topic_id),
        'req_topic': get_object_or_404(Topic, id=topic_id),
        'modules': Module.objects.order_by('id'),
        'topics': Topic.objects.order_by('id'),
        'done_modules': done_modules,
        'done_topics': done_topics,
        'done_questions': done_questions,
        'wrong_questions': wrong_questions,
    }

    return render(request, 'application/question.html', context)

def act(request):
    if '_login' in request.POST:
        return HttpResponseRedirect(reverse('login'))
    elif '_register' in request.POST:
        return HttpResponseRedirect(reverse('application:registration'))

def parse_to_list(string):
    if string:
        return list(map(int, string.split(', ')))
    return []

