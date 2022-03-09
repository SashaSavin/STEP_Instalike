from django.urls import path, include
from accounts.views import ProfilePageView

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('profile/', ProfilePageView.as_view())

]
