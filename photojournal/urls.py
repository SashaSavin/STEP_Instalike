from django.urls import path
from photojournal.views import MainPageView, PageDetailView, HelpPageView, BlogPostLike

urlpatterns = [
    path('', MainPageView.as_view()),
    path('post/<slug:slug>', PageDetailView.as_view(), name='article_detail'),
    path('post/<int:pk>/', PageDetailView.as_view(), name='post-detail'),
    path('post-like/<int:pk>', BlogPostLike, name="post_like"),
    path('help/', HelpPageView.as_view(), name='help'),
]
