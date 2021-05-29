from django.shortcuts import render
from .models import Articles
from django.views.generic import DetailView
from django.apps import apps
from django.core.paginator import Paginator
from django.db.models import Q
user_model = apps.get_model('registration', 'UserProfile')


def article_view(request):
    search_query = request.GET.get('search', '')

    if search_query:
        articles = Articles.objects.filter(Q(title__icontains=search_query) | Q(anons__icontains=search_query))
    else:
        articles = Articles.objects.order_by('-date')
    paginator = Paginator(articles, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if request.user.is_authenticated:
        user_avatar = user_model.objects.filter(user=request.user)
    else:
        user_avatar = False

    return render(request, 'articles/articles_home.html', {'articles': articles,
                                                           'user_avatar': user_avatar,
                                                           'page_obj': page_obj,
                                                           })


class ArticleDetailView(DetailView):
    model = Articles
    template_name = 'articles/detail_view.html'
    context_object_name = 'article'

    def get_context_data(self, *args, **kwargs):
        ua = super().get_context_data(*args, **kwargs)

        if self.request.user.is_authenticated:
            user_avatar = user_model.objects.filter(user=self.request.user)
        else:
            user_avatar = False

        ua['user_avatar'] = user_avatar

        return ua

