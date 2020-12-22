## MiningCollege
**MiningCollege** - проект для мониторинга участия студентов _ГАПОУ КГК_ на мероприятиях.

Для запуска проекта необходимо
1. Клонировать репозиторий:
> ```
> git clone https://github.com/MrSmitix/MiningCollege
> ```
2. Утановить необходимые модули в виртуальном окружении
```pip install -r requirements.txt```
3. Создать миграцию (`manage.py makemigrations`)
    1. Выполнить миграцию  (`manage.py migrate`)
4. Загрузить входные данные (`manage.py loaddata initial_data.json`)
5. Создать суперпользователя (`manage.py createsuperuser`)
6. Запустить веб сервер (`manage.py runserver`)

При желании можно проверить `flake8`
> ```
> $ flake8 --exclude venv, migrations, models --ignore E501
> ```
