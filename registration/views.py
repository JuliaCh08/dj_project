from django.shortcuts import render, redirect
from .forms import RegisterForm, UserProfileForm
from .models import UserProfile


def register(request):
    data = {}
    # Проверка что есть запрос POST
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        user_profile = UserProfileForm(request.POST, request.FILES)
        form.is_valid()
        if form.is_valid() and user_profile.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password1'])
            new_user.save()
            new_user.refresh_from_db()
            new_profile = UserProfile.objects.create(user=new_user, avatar=request.FILES.get('avatar', 'profile_avatar/emptyAvatar.jpg'))
            new_profile.save()
            data['new_user'] = new_user
            data['new_profile'] = new_profile
            return redirect('login')
    else:
        form = RegisterForm()
    new_profile = UserProfileForm()
    data = {'form': form,
            'new_profile': new_profile,
            }

    return render(request, 'registration/register.html', data)



# Create your views here.
