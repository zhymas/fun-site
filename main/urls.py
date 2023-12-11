from django.urls import path
from .views import home, news, create_news, detail_article

urlpatterns = [
    path('', home, name='home'),
    path('news/', news, name='news'),
    path('create_news/', create_news, name='create_news'),
    path('artile/<int:pk>', detail_article, name='detail_article')
]
