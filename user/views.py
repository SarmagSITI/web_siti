from django.shortcuts import render
from django.utils import timezone
from .forms import SignUpForm, SignUpAddition
from .models import UserProfile
from django.http import HttpResponse

# Create your views here.
today = timezone.now().date()
def signup(request):
    # if request.user.is_authenticated:
    #     return HttpResponseRedirect(reverse('user:',))
    if request.method == 'POST':
        user_form = SignUpForm(request.POST)
        user_profile_form = SignUpAddition(request.POST)
        if user_form.is_valid() and user_profile_form.is_valid():
            user = user_form.save()
            # load the profile instance created by the signal
            user.refresh_from_db()
            user.profile.gender = user_profile_form.cleaned_data.get('gender')
            user.profile.phone = user_profile_form.cleaned_data.get('phone')
            user.profile.update_time = today
            user.save()
            return render(request, 'user/success_message.html')
    else:
        user_form = SignUpForm()
        user_profile_form = SignUpAddition()
    context={'user_form' : user_form, 'user_profile_form' : user_profile_form}
    return render (request, 'user/sign_up.html', context)
