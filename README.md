# Image Gallery API (Django + Cloudinary)

## Описание проекта

**REST API** для загрузки, хранения и удаления изображений, созданный с использованием **Django REST Framework** и облачного хранилища **Cloudinary**.

### Функциональность

API предоставляет полный CRUD-функционал для работы с изображениями:

  * **Загрузить** изображение в облако Cloudinary.
  * **Получить список** всех изображений (URL, метаданные).
  * **Посмотреть подробную информацию** об одном изображении.
  * **Удалить** изображение как из базы данных, так и из облака Cloudinary.

### Используемые технологии

  * Python
  * Django
  * Django REST Framework
  * Cloudinary
  * Poetry (Управление зависимостями)
  * `python-decouple` (Работа с `.env`)
  * PostgreSQL (через `psycopg2-binary`)

-----

## Установка и запуск (с использованием Poetry)

### 1\. Клонирование репозитория

```bash
git clone https://github.com/amangulov03/Image-Gallery-API.git
cd Image-Gallery-API
```

### 2\. Установка зависимостей
# Активирует виртуальное окружение, созданное Poetry
poetry shell

Проект использует **Poetry** для управления зависимостями. Установите все необходимые пакеты и создайте виртуальное окружение:

```bash
# Убедитесь, что Poetry установлен в вашей системе
poetry install
```

### 3\. Настройка Cloudinary

Создайте аккаунт на [Cloudinary](https://cloudinary.com) и получите данные для подключения: `CLOUD_NAME`, `API_KEY`, `API_SECRET`.

Эти данные будут использоваться в вашем `settings.py` и файле `.env`.

### 4\. Создание файла `.env`

Создайте файл `.env` в корне вашего проекта (рядом с `manage.py`) и добавьте в него следующие строки, заменив значения на свои:

```env
# Django
SECRET_KEY=ваш-секретный-ключ

# Cloudinary Secret (API_SECRET берется из .env, остальные можно прописать в settings.py)
API_SECRET=ваш-api-секрет-от-Cloudinary

# PostgreSQL Database (настройки могут отличаться в зависимости от вашего провайдера)
DB_NAME=ваше имя в базе данных
DB_USER=ваш-пользователь-базы данных
DB_PASSWORD=ваш пароль к базе данных
DB_HOST=localhost
DB_PORT=5432
```

### 5\. Конфигурация Cloudinary в `settings.py`

Убедитесь, что в вашем `conf/settings.py` прописана конфигурация Cloudinary:

```python
# settings.py (пример конфигурации)
import cloudinary
from decouple import config

# ...

cloudinary.config(
    cloud_name = 'ваше имя в облаке',   # Замените на ваше имя облака
    api_key = 'ваш api key',           # Замените на ваш API Key
    api_secret = config('API_SECRET'), # Получаем из .env
    secure=True
)
```

### 6\. Миграции и запуск проекта

Используйте команду `poetry run` для запуска команд в виртуальном окружении Poetry:

```bash
# Создание и применение миграций
poetry run python manage.py makemigrations
poetry run python manage.py migrate

# Запуск сервера
poetry run python manage.py runserver
```

После запуска сервер будет доступен по адресу: **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)**

-----

## API Эндпоинты

| Метод | URL | Описание |
| :---: | :--- | :--- |
| `POST` | `/api/images/` | Загрузка изображения. |
| `GET` | `/api/images/` | Получить список всех изображений. |
| `GET` | `/api/images/<id>/` | Получить информацию об одном изображении. |
| `DELETE` | `/api/images/<id>/` | Удалить изображение (из БД и из Cloudinary). |

## Примеры `curl`-запросов

### 1\. Загрузка изображения (`POST`)

```bash
curl -X POST http://127.0.0.1:8000/api/images/ \
  -F "title=Мой фото" \
  -F "description=Фото на улице" \
  -F "file=@/путь/к/твоему/my_photo.jpg"
```

### 2\. Получение списка изображений (`GET`)

```bash
curl -X GET http://127.0.0.1:8000/api/images/
```

### 3\. Получение информации об одном изображении (`GET`)

```bash
curl -X GET http://127.0.0.1:8000/api/images/1/
```

### 4\. Удаление изображения (`DELETE`)

```bash
curl -X DELETE http://127.0.0.1:8000/api/images/1/
```

-----

## Структура проекта

```
image_gallery_project/
│
├── images/
│   ├── models.py          # Модель ImageItem
│   ├── serializers.py     # Сериализатор
│   ├── views.py           # ViewSet с логикой Cloudinary
│   └── urls.py            # Маршрутизация API для приложения
│
├── conf/
│   ├── settings.py        # Настройки проекта и Cloudinary
│   └── urls.py            # Главная маршрутизация API
│
├── .env                   # Конфиденциальные настройки (SECRET_KEY, DB, API_SECRET)
├── poetry.lock            # Зафиксированные зависимости
├── pyproject.toml         # Зависимости проекта (для Poetry)
└── manage.py
```

-----

## Автор

**Ванюхин Тимофей** — Python/Django Developer — стажёр.
