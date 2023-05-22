# Этот файл нужен чтобы связать страничку create с базой данных
# Сначала из док-та models мы импортиируем наш класс Articles
# На основе ModelForm из django.forms мы создадим свой собственный
from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea
# Описываем класс и его работу с моделью в models.py
class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        # Описываем поля которые будут выведены в форме
        fields = ['title','anons','full_text','date']
        # Добавляем полям 'title','anons'.. различные атрибуты. Они написаны в create.html!
        widgets ={
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название статьи'
            }),
            "anons": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Анонс статьи'
            }),
            "date": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата публикации'
            }),
            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст статьи'
            })
        }