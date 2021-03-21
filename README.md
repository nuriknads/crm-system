# 🏢 Django CRM API

## 📌 Описание:
CRM-система для управления клиентами, сделками и задачами. Построена на **Django + Django REST Framework** с JWT-аутентификацией и документацией Swagger.

---

## 🚀 Функционал:
- Управление клиентами (создание, редактирование, удаление)
- Управление сделками (сумма, статус, клиент)
- Управление задачами по сделкам
- Авторизация через **JWT**
- Документация API через **Swagger**

---

## 🛠 Стек технологий:
- Python 3.x
- Django 4.x
- Django REST Framework
- SimpleJWT (JWT-аутентификация)
- drf-yasg (Swagger)
- SQLite (по умолчанию)
- Git / GitHub

---

## 🔗 API эндпоинты:
- `POST /api/token/` — получить JWT токен
- `GET /api/clients/` — список клиентов
- `GET /api/deals/` — список сделок
- `GET /api/tasks/` — список задач

---

## ▶ Запуск проекта:
```bash
git clone https://github.com/nuriknads/crm-system.git
cd crm-system
python -m venv venv
source venv/bin/activate  
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
# Commit 6 — 2021-02-16
# Commit 9 — 2021-02-25
# Commit 14 — 2021-03-12
# Commit 15 — 2021-03-15
# Commit 21 — 2021-04-02
# Commit 23 — 2021-04-08
# Commit 26 — 2021-04-17
# Commit 28 — 2021-04-23
# Commit 31 — 2021-05-02
# Commit 32 — 2021-05-05
# Commit 33 — 2021-05-08
# Commit 40 — 2021-05-29
# Commit 41 — 2021-06-01
# Commit 47 — 2021-06-19
# Commit 48 — 2021-06-22
# Commit 53 — 2021-07-07
# Commit 62 — 2021-08-03
# Commit 69 — 2021-08-24
# Commit 2 — 2021-02-04
# Commit 13 — 2021-03-09
# Commit 15 — 2021-03-15
# Commit 17 — 2021-03-21
