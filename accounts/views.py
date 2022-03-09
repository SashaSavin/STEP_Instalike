from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from .models import Profile


class ProfilePageView(LoginRequiredMixin,ListView):
    model = Profile
    template_name = 'profile.html'
    context_object_name = 'profile'

