from audioop import reverse

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView
from photojournal.models import Post


class MainPageView(LoginRequiredMixin,ListView):
    model = Post
    template_name = 'main.html'
    context_object_name = 'posts'


def BlogPostLike(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return HttpResponseRedirect('/')

class PageDetailView(LoginRequiredMixin,DetailView):
    model = Post
    template_name = 'detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        likes_connected = get_object_or_404(Post, id=self.kwargs['pk'])
        liked = False
        if likes_connected.likes.filter(id=self.request.user.id).exists():
            liked = True
        data['number_of_likes'] = likes_connected.number_of_likes()
        data['post_is_liked'] = liked
        return data


class HelpPageView(LoginRequiredMixin, TemplateView):
    template_name = 'help.html'


