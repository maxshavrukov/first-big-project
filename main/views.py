from django.shortcuts import render

# Create your views here.
# Этот файл отвечает за те методы которые будут вызваны, при переходе пользователя на ту или иную страницу.
# Например! Пользователь перейдет на главную страницу, значит мы отслеживаем это в /itproger/urls.py. Дальше мы из urls.py
# вызовем файл views.py, и в нем же вызовем определнный метод который покажет пользователю определенную html страницу.

# Этоти методы созданы для maurls.py
def index(request): # Параметр request это другими словами "запрос"
    data = {
        'title': 'Главная страница',
        'values': ['Some', 'Hello', '123'], # Параметр values имеет внутри себя список, который мы можем вывести в index.html
        'obj': ['age', 'car', 'hobby']
    }
    return render(request,'main/index.html', data) # С помощью метода render можно показывать целые html шаблоны используя их названия и путь к ним
# А вот и тот самый 'about', про который мы писали в main\urls.py           # В теге {title} мы передаем шаблон
def about(request):
    return render(request,'main/about.html')

