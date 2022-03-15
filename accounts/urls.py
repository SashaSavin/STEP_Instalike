from django.urls import path, include
from accounts.views import ProfilePageView, UserProfilePersonalPostsView, UserProfileSavesView, UserProfileEditPageView, \
    CreatePostView, UserPersonalPostsUpdateView, UserPersonalPostsDeleteView

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('profile/', ProfilePageView.as_view()),

    path('profile/posts', UserProfilePersonalPostsView.as_view(), name='user_posts'),
    path('profile/posts/edit/<int:pk>', UserPersonalPostsUpdateView.as_view(), name='profile_post_edit'),
    path('profile/posts/delete/<int:pk>', UserPersonalPostsDeleteView.as_view(), name='profile_post_delete'),

    path('profile/saves', UserProfileSavesView.as_view(), name='user_saves'),
    path('profile/updates/', UserProfileEditPageView.as_view(), name='user_update'),
    path('profile/create', CreatePostView.as_view(), name='post_create'),



]
