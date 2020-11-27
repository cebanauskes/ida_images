# IDA_images
Веб приложение, позволяющее загружать и просматривать изображения, также можно менять размер любого загруженного изображения

# Стек
Python, Django, SQLite, Pillow

# Инструкция по развертыванию проекта 
1. Скачать проект или клонировать с помощью git (`git clone https://github.com/cebanauskes/ida_images.git`)
2. Перейти в каталог с проектом и создать виртуальное окружение (`python3 -m venv venv`)
3. Запустить виртуальное окружение (`source venv/bin/activate`) на Mac/Linux или (`source venv/Scripts/activate`) на Windows
4. Установить все необходимые пакеты, указанные в файле requirements.txt (`pip install -r requirements.txt`)
5. Запустить миграции (`python manage.py migrate`)
6. Для проверки работы проекта запустить тестовый сервер (`python manage.py runserver`)
7. Перейти по адресу http://127.0.0.1:8000
