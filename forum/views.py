from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ForumForm, AnswerForm
from .models import Forum, Answer
from django.apps import apps
from django.db.models import Q

user_model = apps.get_model('registration', 'UserProfile')


@login_required(redirect_field_name='redirect_to', login_url='/accounts/login/')
def forum_view(request):
    search_query = request.GET.get('search', '')

    if search_query:
        forum = Forum.objects.filter(Q(title__icontains=search_query) | Q(full_text__icontains=search_query))
        answer = Answer.objects.filter(full_answer__icontains=search_query)
    else:
        forum = Forum.objects.order_by('-date')
        answer = Answer.objects.order_by('-date')
    if request.user.is_authenticated:
        user_avatar = user_model.objects.filter(user=request.user)
    else:
        user_avatar = False

    return render(request, 'forum/forum.html', {'forum': forum,
                                                'answer': answer,
                                                'user_avatar': user_avatar})


def questions(request):
    if request.user.is_authenticated:
        user_avatar = user_model.objects.filter(user=request.user)
    else:
        user_avatar = False
    error = ''
    if request.method == 'POST':
        form = ForumForm(request.POST)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user

            instance.save()
            return redirect('forum')

    else:
        error = 'Неверно заполнены поля'

    form = ForumForm()

    data = {'form': form,
            'error': error,
            'user_avatar': user_avatar
            }

    return render(request, 'forum/questions.html', data)


def answer(request, id):
    if request.user.is_authenticated:
        user_avatar = user_model.objects.filter(user=request.user)
    else:
        user_avatar = False

    if request.method == 'POST':
        form_answer = AnswerForm(request.POST)

        if form_answer.is_valid():
            new_answer = form_answer.save(commit=False)
            new_answer.user = request.user
            new_answer.forum_id = id
            new_answer.save()
            return redirect('forum')

    form_answer = AnswerForm()

    return render(request, 'forum/answers.html',
                  {'form_answer': form_answer,
                   'user_avatar': user_avatar,
                   })



# Create your views here.

