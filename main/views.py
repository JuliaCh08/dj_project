from django.db.models import Q
from django.shortcuts import render
from .models import BlockInfo
from django.views.generic import DetailView
from django.apps import apps

model = apps.get_model('registration', 'UserProfile')


def index(request):
    search_query = request.GET.get('search', '')

    if search_query:
        dog_info = BlockInfo.objects.filter(Q(title__icontains=search_query) | Q(anons__icontains=search_query))
    else:
        dog_info = BlockInfo.objects.all()
    if request.user.is_authenticated:
        user_avatar = model.objects.filter(user=request.user)
    else:
        user_avatar = False

    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    return render(request, 'main/index.html', {'dog_info': dog_info,
                                               'user_avatar': user_avatar,
                                               'num_visits': num_visits})


class DogBreedDetailView(DetailView):
    model = BlockInfo
    template_name = 'main/dog_info.html'
    context_object_name = 'dog_breed_info'

    def get_context_data(self, *args, **kwargs):
        ua = super().get_context_data(*args, **kwargs)
        if self.request.user.is_authenticated:
            user_avatar = model.objects.filter(user=self.request.user)
        else:
            user_avatar = False

        ua['user_avatar'] = user_avatar

        return ua


def policy(request):
    return render(request, 'main/Privacy_Policy.html')
