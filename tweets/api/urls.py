from django.conf.urls import url
from .serializers import TweetModelSerializer
from .views import TweetListAPIView,TweetCreateAPIView

app_name = 'tweet'
urlpatterns = [
    url(r'^$', TweetListAPIView.as_view(),name="list"),
    url(r'^create/$', TweetCreateAPIView.as_view(), name='create'),
]
