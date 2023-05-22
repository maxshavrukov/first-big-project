# Эти url адресса принадлежат части сайта "news"
from django.urls import path
from . import views

urlpatterns = [
    path('',views.news_home, name='news_home'), # Сдесь всегда пусто в '', потому что мы уже понимаем что мы на главной странице news!
    # Тут созается страница на которой, можно создавать записи!
    path('create', views.create, name='create'),
    path('<int:pk>',views.NewsDetailView.as_view(), name='news-detail'), # Сдесь создаем новую переменную для отслеживания динамических страниц
    # Тут создается страница на которой, можно редактировать записи!
    path('<int:pk>/update',views.NewsUpdateView.as_view(), name='news-update'),
    # Тут создается страница на которой, можно удалять записи!
    path('<int:pk>/delete',views.NewsDeleteView.as_view(), name='news-delete'),
]

