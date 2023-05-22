"""itproger URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# Нужно подгрузить статику и настройки!
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Тут написано, что при переходе по URL адрессу 'admin' у нас будет открываться приложение 'admin.site.urls' (Панель администратора)
    # Все функции сдесь используют path!
    path('admin/', admin.site.urls),
    # Мы хотим отслеживать главную страницу. Пишем это, вверх добавлем метод include. Теперь нужно создать в main файл urls.py
    # В скобках 1 директория, 2 файл.
    path('', include('main.urls')),
    # Подключаем еще одну часть сайта "news", и когда пользователь будет на них переходить и обработка будет в "news.urls"
    path('news/', include('news.urls')),
    path('weather/', include('weather.urls'))
    
    # Это необхоимо для работы CSS в папке static!
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
