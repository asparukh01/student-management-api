# Student Management API

Это проект для управления студентами и их оценками, построенный с использованием FastAPI и SQLAlchemy.


## Установка

1. Клонируйте репозиторий:

    git clone https://github.com/asparukh01/student-management-api.git
    cd student-management-api

2. Создайте и активируйте виртуальное окружение:

    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. Установите зависимости:

    pip install -r requirements.txt

4. Настройте базу данных. Убедитесь, что у вас установлен SQLite (или другой, если вы используете другой движок). Файл базы данных будет создан автоматически при первом запуске.


## Запуск приложения

1. Запустите приложение:

    можно запустить это команодой `uvicorn main:app --reload`
    можно просто запустив файл `main.py`

2. Откройте браузер и перейдите по адресу http://127.0.0.1:8000 для доступа к API.

3. Документация Swagger будет доступна по адресу http://127.0.0.1:8000/docs, а документация ReDoc по адресу http://127.0.0.1:8000/redoc.


## Использование API эндпоинтов

### Студенты

- Создать студента POST /student/

    Пример тела запроса:
    
    ```
    {
    "first_name": "John",
    "last_name": "Doe",
    "phone_number": "1234567890",
    "email": "john.doe@example.com",
    "class_name": "10A"
    }
- Получить студента по ID GET /student/{student_id}/
    
    Пример: `/student/1/`

- Обновить студента PATCH /student/{student_id}/

    Пример тела запроса:    
    ```
    {
    "first_name": "John",
    "last_name": "Doe",
    "phone_number": "0987654321",
    "email": "john.doe@example.com",
    "class_name": "10B"
    }
- Удалить студента DELETE /student/{student_id}/

    Пример: `/student/1/`

### Оценки

- Создать оценку POST /score/

    Пример тела запроса:
    ```
    {
    "student_id": 1,
    "subject": "Math",
    "grade": 95
    }
- Получить оценку по ID  GET /score/{score_id}/

    Пример: `/score/1/`

- Обновить оценку PATCH /score/{score_id}/

    Пример тела запроса:
    ```
    {
    "subject": "Math",
    "grade": 98
    }
- Удалить оценку DELETE /score/{score_id}/

    Пример: `/score/1/`