from django.db import models
# После завершения работы с моделями нужно сделать МИГРАЦИЮ чтобы объявить ее в базе данных!
# Create your models here. Создаем таблицу в базе данных
# Создаем класс с именем и говорим ему в () что он наследует все от класа Model
class Articles(models.Model):
    # В поле title вводим строки и для нее использовать клас CharField(макс 250 симв) и TextField (до 10к симв)
    title = models.CharField('Название', max_length=50, default='')
    anons = models.CharField('Анонс', max_length=250, default='')
    full_text = models.TextField('Статья')
    # Ну DateTimeField все понятно и так да?
    date = models.DateTimeField('Дата публикации')
    # Магический метод _str_
    def __str__(self):
        return self.title
    # Этот метод обязателен, он говорит на какую страничку будет переадрессовывать пользователя после обновления статьи
    def get_absolute_url(self):
        return f'/news/{self.id}'

    # Сдесь мы меняем отображение имени для Articles в панели администрирования!
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

