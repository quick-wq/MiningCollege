# MiningCollege
MiningCollege - проект для мониторинга участия студентов ГАПОУ КГК на мероприятиях.

Для запуска проекта необходимо
0. Создать виртуальное окружение и установить необходимые модули (pip install -r requirements.txt)
1. Создать миграций (manage.py makemigrations)
2. Выполнить миграций (manage.py migrate)
3. Загрузить входные данные (manage.py loaddata initial_data.json)
4. Создать суперпользователя (manage.py createsuperuser)
5. Запустить веб сервер (manage.py runserver)

При желаний можно проверить flake8
$ flake8 --exclude venv,migrations,models --ignore E501
