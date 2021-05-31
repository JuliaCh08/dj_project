from django.shortcuts import render, redirect
from .forms import RegisterForm, UserProfileForm
from .models import UserProfile
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


def register(request):
    error_p = ''
    data = {}
    # Проверка что есть запрос POST
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        user_profile = UserProfileForm(request.POST, request.FILES)

        if form.is_valid() and user_profile.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password1'])
            new_user.save()
            new_user.refresh_from_db()
            new_profile = UserProfile.objects.create(user=new_user, avatar=request.FILES.get('avatar', 'profile_avatar/emptyAvatar.jpg'))
            new_profile.save()
            data['new_user'] = new_user
            data['new_profile'] = new_profile
            """html_body = render_to_string("registration/password_reset_email.html", data)
            msg = EmailMultiAlternatives(subject='Сброс пароля', to=['mail@gmail.com'])
            msg.attach_alternative(html_body, "text/html")
            msg.send()"""
            return redirect('login')
        else:
            error_p = form.clean_password2()

    form = RegisterForm()
    new_profile = UserProfileForm()
    data = {'form': form,
            'error_p': error_p,
            'new_profile': new_profile,
            }
    return render(request, 'registration/register.html', data)



# Create your views here.
