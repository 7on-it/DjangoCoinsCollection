# 🪙 Django Coins Collection

Веб-приложение для управления личной коллекцией монет.  
Учебный проект по курсу **"Python on Web" (Django)**.

---

## 🚀 Быстрый старт

### 1. Клонируй репозиторий
```bash
git clone https://github.com/7on-it/DjangoCoinsCollection.git
cd DjangoCoinsCollection
```

### 2. Создай и активируй виртуальное окружение

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Mac / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Установи зависимости
```bash
pip install -r requirements.txt
```

### 4. Примени миграции (создай базу данных)
```bash
python manage.py migrate
```

### 5. Создай суперпользователя (для входа в админку)
```bash
python manage.py createsuperuser
```

### 6. Запусти сервер
```bash
python manage.py runserver
```

### 7. Открой в браузере
- **Главная страница:** [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- **Админка:** [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## 🔑 Функционал

- ✅ Просмотр коллекции монет (главная страница)
- ✅ Детальная информация о каждой монете
- ✅ Административная панель для управления коллекцией
- ✅ Регистрация и аутентификация пользователей
- ✅ Хеширование паролей (встроено в Django)
- ✅ Загрузка фотографий монет (через админку)

---

## 🛠️ Технологии

- **Django** — веб-фреймворк
- **SQLite** — база данных (по умолчанию)
- **Bootstrap 5** — стилизация
- **Pillow** — работа с изображениями

---

## 📁 Структура проекта

```
DjangoCoinsCollection/
├── core/                # Настройки проекта
├── coins/               # Основное приложение
├── templates/           # HTML-шаблоны
├── media/               # Загруженные фото (не в Git)
├── manage.py
├── requirements.txt
└── README.md
```

---

## ✨ Автор

**7on-it** — учебный проект 2026
