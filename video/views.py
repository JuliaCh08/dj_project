from django.shortcuts import render
from .models import Videos
from django.apps import apps

model = apps.get_model('registration', 'UserProfile')


def video(request):
    video_content = Videos.objects.all()
    if request.user.is_authenticated:
        user_avatar = model.objects.filter(user=request.user)
    else:
        user_avatar = False
    return render(request, 'video/video_content.html', {'video_content': video_content,
                                                        'user_avatar': user_avatar})

