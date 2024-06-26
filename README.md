
<h1 align="center">  Myassist - приложение для составления списка необходимых продуктов </h1>


<p>
    <a href= "https://github.com/VitaliyDrozdov/foodgram/actions/">
    <img alt="GitHub - Test status" src="https://github.com/VitaliyDrozdov/foodgram/actions/workflows/main.yml/badge.svg">
    </a>
</p>
<h2 align="center">Разработано на технологиях</h2>

<p align="center">
    <a href="https://www.python.org/">
	    <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54">
    </a>
    <br>
    <a href="https://www.docker.com/">
	    <img alt="docker" src="https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white">
     </a>
    <a href="https://www.djangoproject.com/">
        <img alt="Django" src="https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white">
    </a>
    <a href="https://www.django-rest-framework.org/">
        <img alt="Django-REST-Framework" src="https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray">
    </a>
    <a href="https://www.postgresql.org/">
        <img alt="PostgreSQL" src="https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white">
    </a>
	 <br>
    <a href="https://gunicorn.org/">
        <img alt="gunicorn" src="https://img.shields.io/badge/gunicorn-%298729.svg?style=for-the-badge&logo=gunicorn&logoColor=white">
    </a>
    <a href="https://nginx.org/ru/">
        <img alt="Nginx" src="https://img.shields.io/badge/nginx-%23009639.svg?style=for-the-badge&logo=nginx&logoColor=white">
    </a>
  
</p>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Содержание</summary>

- [📍 Описание](#-описание)
- [🚀 Запуск проекта](#-запуск)
- [⚙️ Загрузить данные](#️-Загрузить)
- [🤖 Документация](#-Документация)
- [🧪 Примеры запросов](#-Примеры)
- [🛠 Ссылка на сайт](#-Ссылка)
- [📄 Автор](#-автор)
</details>
<hr>  


</p>
<h2 align="center">

## 📍 Описание

</h2>
<p>
    Goods assistant - помогает составить список продуктов для покупок на основе рецептов. Позволяет публиковать рецепты, сохранять избранные, а также формировать список покупок для выбранных рецептов. Можно подписываться на любимых авторов.
</p>


<h2 align="center">

## 🚀 Запуск

</h2>

<p>
-Скачать проект по SSH:

```text
git clone git@github.com:VitaliyDrozdov/foodgram.git
```

Установить зависимости:
> ```console
> $ pip install -r requirements.txt
> ```

- Создать .env файл в директории app/backend/foodgram/ (рядом с manage.py):

```text
touch .env
```

- Пример заполнения .env файла:

```text
POSTGRES_DB=example_db
POSTGRES_USER=example_user
POSTGRES_PASSWORD=example_password
DB_NAME=foodgram
DB_HOST=db
DB_PORT=5432
DEBUG = False
DJANGO_SECRET_KEY=some_key
ALLOWED_HOSTS = foodgramdr.hopto.org, localhost, 127.0.0.1
CSRF_TRUSTED_ORIGINS = https://foodgramdr.hopto.org
USE_SQLITE=False
```

- Перейти в папку infra и запустить docker-compose:

```text
sudo docker-compose -f docker-compose.production.yml up -d
```

Создать суперпользователя:

```text
sudo docker exec -it foodgram-back python manage.py createsuperuser
```
</p>

## ⚙️ Загрузить

```text
sudo docker exec foodgram-back python manage.py import_data
```
Зайти в админку и создать несколько тэгов.

## 🧪 Примеры

```text
http
  GET /api/recipes/
```
```text
http
  GET /api/recipes/{id}/
```
Более подробно запросы и ответы описаны в документации.

## 🤖 Документация

```text
https://foodgramdr.hopto.org/api/docs/

```
## 🛠 Ссылка
<h3>
<!--     <a href="https://foodgramdr.hopto.org/">https://foodgramdr.hopto.org/</a> -->
</h3>

## Автор :

[VitaliyDrozdov](https://github.com/VitaliyDrozdov)
