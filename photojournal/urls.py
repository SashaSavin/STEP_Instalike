from django.urls import path
from photojournal.views import MainPageView, PageDetailView, HelpPageView

urlpatterns = [
    path('', MainPageView.as_view()),
    path('post/<int:pk>/', PageDetailView.as_view(), name='post-detail'),
    path('help/', HelpPageView.as_view(), name='help'),
]
