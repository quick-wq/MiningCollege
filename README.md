# MiningCollege
MiningCollege - проект для мониторинга участия студентов ГАПОУ КГК на мероприятиях.

Для запуска проекта необходимо
1. Создать виртуальное окружение и установить необходимые модули (pip install -r requirements.txt)
2. Создать миграций (manage.py makemigrations)
3. Выполнить миграций (manage.py migrate)
4. Загрузить входные данные (manage.py loaddata initial_data.json)
5. Создать суперпользователя (manage.py createsuperuser)
6. Запустить веб сервер (manage.py runserver)

При желаний можно проверить flake8
$ flake8 --exclude venv,migrations,models --ignore E501
