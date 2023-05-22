from django.shortcuts import render, redirect
# Нужно импортировать тот класс (табличку/модель) с которой хотим работать
from .models import Articles
# Импортируем из forms.py наш класс ArticlesForm
from .forms import ArticlesForm
# Импортируем это для динамических страниц и редактирования записей!
from django.views.generic import DetailView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

def news_home(request):
    # В news= мы написали что хотим получить полностью все объекты (all), или сортировка (order_by('title или date'))
    news = Articles.objects.order_by('-date')
    # А передавать мы их будем внутрь шаблона. Это написано третим атрибутом "news" ниже.
    return render (request, 'news/news_home.html', {'news': news})

# Создаем класс для динамических страниц
class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/details_views.html'
    context_object_name = 'article'

# Создаем класс для редактирования записей! Мы уже его импортировали выше! А так же создали в urls.py!
class NewsUpdateView(UpdateView):
    model = Articles
    template_name = 'news/create.html' #Используем шаблона метода create, так как он логически подходит под редактирование
    # Объявляем то что будет отображатся в форме
    form_class = ArticlesForm

# Создаем класс для удаления записей! Мы уже его импортировали выше! А так же создали в urls.py!
class NewsDeleteView(DeleteView):
    model = Articles
    success_url = '/news/'
    template_name = 'news/news-delete.html' #Используем уже другой шаблон! Его нужно создать!

# Создаем функцию create для добавления записей.
def create(request):
    error=''
    # Получение данных из формы
    if request.method == 'POST':
        # Создаем новый объект в котором будут хранится данные передаваемые пользователем
        form = ArticlesForm(request.POST)
        # Форма is_valid проверяет корректно ли введены данные от пользователя.
        if form.is_valid():
            # Если данные корректны то мы сохраним эти данные
            form.save()
            # После сохранения нас будет перебрасывать на главную страницу home
            return redirect('news_home')
            # А если не корректно, то будет выводится ошибка error, который мы прописали в шаблоне data чуть ниже!
        else: error = 'Форма была неверной'

    form = ArticlesForm()
    # Отображения формы (ввод статьи и анонса) 
    data = {
        'form': form,
        'error': error
    }

    return render (request, 'news/create.html', data) # date - указывает на то что я буду передовать в словарь! Не забудь за нее
                                                      # Так же в create.html нужно написать {{ form }}, что бы она появилась!

