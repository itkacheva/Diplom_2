# Тестирование ручек API (Диплом.Часть 2).

Автотесты API ручек для Stellar Burgers (https://stellarburgers.nomoreparties.site/).

Эндпойнты описаны в документации API (https://code.s3.yandex.net/qa-automation-engineer/python-full/diploma/api-documentation.pdf?etag=3403196b527ca03259bfd0cb41163a89).

## Установка

1. Склонируйте репозиторий на локальную машину:

git clone https://github.com/your_username/your_project.git

2. Перейдите в каталог проекта:

cd your_project

3. Создайте виртуальное окружение и активируйте его:

python -m venv venv
venv\Scripts\activate (Windows)
source venv/bin/activate (Linux/Mac)

4. Установите зависимости:

pip install -r requirements.txt

## Запуск тестов

1. Перейдите в каталог с тестами:

cd tests

2. Запустите тесты с помощью pytest:

pytest

## Структура проекта

Проект имеет следующую структуру:

- endpoints/ - Содержит модули с API-эндпоинтами
  - ingredients_endpoints.py - Модуль с эндпоинтами ингредиентов
  - order_endpoints.py - Модуль с эндпоинтами заказов
  - user_endpoints.py - Модуль с эндпоинтами пользователей

- services/ - Содержит вспомогательные модули для генерации данных и запросов
  - gen_fake_email.py - Модуль для генерации фейковых email-адресов
  - gen_ingredients_data.py - Модуль для генерации данных об ингредиентах
  - gen_random_string.py - Модуль для генерации случайных строк
  - gen_user_data.py - Модуль для генерации данных пользователей

- tests/ - Содержит файлы тестов для различных функциональностей
  - test_order_create.py - Скрипт тестирования создания заказа
  - test_order_get.py - Скрипт тестирования получения заказов
  - test_user_creat.py - Скрипт тестирования создания пользователей
  - test_user_data_chang.py - Скрипт тестирования изменения данных пользователя
  - test_user_login.py - Скрипт тестирования входа пользователя

