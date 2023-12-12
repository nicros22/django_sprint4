# Описание проекта
Одна и проектных работ под названием Blogicum, в которой мы использовали CBV, реализовали права доступа пользователей, добавили работу с изображениями и регистрацию на сайте.
# Стэк
- Python 3.11.4
- Django 3.2.16
# Руководство по запуску локально
## Установить репозиторий по `ssh`: 

```sh 

git clone git@github.com:nicros22/django_sprint4.git

```



## Создать виртуальное окружение: 

```sh 

python -m venv venv 

``` 

 

## Активировать виртуальное окружение: 

```sh 

source venv/Scripts/activate

``` 

 

## Установить `зависимости`: 

```sh 

pip install -r requirements.txt

``` 



## Перейти в папку проекта: 

```sh 

cd blogicum

``` 



 ## Загрузить фикстуры: 

```sh 

python manage.py loaddata db.json

```



## Установить `миграции`: 

```sh 

python manage.py migrate 

``` 

 

## Запустить `проект`: 

```sh 

python manage.py runserver 

``` 

 

## Создать суперпользователя:

```sh 

python manage.py createsuperuser 

```



Автор:
Никита Пономаренко
