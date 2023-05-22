import requests #requests нужно установить с помощью pip install requests!
from django.shortcuts import render, redirect
from .models import City
from .forms import CityForm

# Сдесь мы пишем функцию index в которой указываем id с сайта и специальный url
def index(request):
    appid = '01b601dd9ab0ed8a41657aba07317468'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid

    err_msg = ''
    massage = ''
    massage_class = ''

    if (request.method == 'POST'):
        form = CityForm(request.POST)
        # Проверка городов, которые уже есть
        if form.is_valid():
            new_city = form.cleaned_data['name']
            city_count = City.objects.filter(name__iexact = new_city).count()
            # Проверка городов которых не существует
            if city_count == 0:
                res = requests.get(url.format(new_city)).json()
                if res['cod'] == 200: #200 Берется из json, нужно написать print(res) чтобы попал ответ в терминал, и там будет эти 200! 
                    form.save()    
                else:
                    err_msg ='Города не существует'
            else:
                err_msg = 'Город уже добавлен'

        if err_msg:
            massage = err_msg
            massage_class = 'is-danger'
        else:
            massage = 'Город успешно добавлен'
            massage_class = 'is_success'

    form = CityForm()

    cities = City.objects.all()
    # Список all_cities внутри которого будут наши города со своей информацией
    all_cities = []
    # То, что будет хранить один элемент списка city в списке cities
    for city in cities:
        # Запрос api на нужный нам город
        res = requests.get(url.format(city.name)).json()
        city_info = {
                'city': city.name,
                'temperature': res['main']['temp'],
                'temp_min': res['main']['temp_min'],
                'temp_max': res['main']['temp_max'],
                'clouds': res['clouds']['all'],
                'winds': res['wind']['speed'],
            }
        # Добавление нового элемента с помощью append
        all_cities.append(city_info)
        
    context = {
        'all_info': all_cities,
        'form': form,
        'massage': massage,
        'massage_class': massage_class        
        }
 
    return render(request, 'weather/weather-home.html', context)

# Фунцкия удаления элемента списка (города) 
def delete_city(requset, city_name):
    City.objects.get(name=city_name).delete()
    return redirect('weather-home')
 