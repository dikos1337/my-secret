# [Попробовать сервис можно тут](https://dikos1337.pythonanywhere.com/)

# Запуск под Linux (для разработки)

Для начала надо скачать проект и установить зависимости.
```sh
$ git clone https://github.com/dikos1337/my-secret
$ cd my-secret
$ npm install
$ cd backend
$ python -m venv venv
$ . venv/bin/activate
$ pip install -r requirements.txt
```
Cделать миграции и cоздать супер пользователя.
```sh
(venv) /backend$ python manage.py makemigrations
(venv) /backend$ python manage.py migrate
(venv) /backend$ python manage.py createsuperuser
```
Запуск frontend
```sh
$ npm run serve
```
Запуск backend
```sh
(venv) /backend$ python manage.py runserver
```
Запуск celery (нужен запущенный redis сервер)
```sh
(venv) /backend$ celery -A core worker -l info -B
```

# Скриншоты

<!-- https://imgur.com/a/rrCxAYl -->

### Главная страница:

![alt text](https://i.imgur.com/TsYnAKs.png)

### Страница после создания секрета:

![alt text](https://i.imgur.com/oGEBHS0.png)

### Страница с требованием пароля

![alt text](https://i.imgur.com/Rp52g8L.png)

![alt text](https://i.imgur.com/axzca8g.png)

### Страница с секретом

![alt text](https://i.imgur.com/1UJJEK5.png)

### Если после просмотра секрета обновить страницу
![alt text](https://i.imgur.com/OdAVnkJ.png)
