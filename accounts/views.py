from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, UpdateView, CreateView, FormView, DeleteView

from .forms import ProfileEditForm
from .models import Profile
from photojournal.models import Post


class ProfilePageView(LoginRequiredMixin,ListView):
    model = Profile
    template_name = 'profile.html'
    context_object_name = 'profile'

    def get_object(self):
        return get_object_or_404(Profile, user=self.kwargs['slug'])


class UserProfilePersonalPostsView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'user_blog.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)


class UserPersonalPostsDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    context_object_name = "post"
    template_name = 'post_confirm_delete.html'
    success_url = "/"


class UserPersonalPostsUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['photo', 'message']
    template_name = 'user_post_update.html'
    success_url = "/"


class UserProfileSavesView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'user_blog.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)


class UserProfileEditPageView(LoginRequiredMixin, FormView):
    form_class = ProfileEditForm
    template_name = 'profile_update.html'
    success_url = "/"


class CreatePostView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['author', 'photo', 'message']
    template_name = 'post_create.html'
    success_url = "/"

    def form_valid(self, form):
        form.save()
        return super(CreatePostView, self).form_valid(form)

