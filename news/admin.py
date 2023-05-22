from django.contrib import admin
from .models import Articles
# Register your models here.
# Нужно зарегистрировать модель/таблицу в этом документе, чтобы видеть ее в панели администратора
# Регистрация ссылается на Articles после МИГРАЦИИ
admin.site.register(Articles)

