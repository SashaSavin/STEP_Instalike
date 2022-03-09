from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, TemplateView
from photojournal.models import Post


class MainPageView(LoginRequiredMixin,ListView):
    model = Post
    template_name = 'main.html'
    context_object_name = 'posts'


class PageDetailView(LoginRequiredMixin,DetailView):
    model = Post
    template_name = 'detail.html'
    context_object_name = 'post'


class HelpPageView(LoginRequiredMixin, TemplateView):
    template_name = 'help.html'

