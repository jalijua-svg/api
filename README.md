# LibraryAPI

API для системы на Django REST Framework

## Документация

* Swagger UI: http://127.0.0.1:8000/api/schema/swagger-ui/
* Схема: http://127.0.0.1:8000/api/schema/

## Функционал

* CRUD для авторов, категорий, издательств, книг, читателей, книжных карточек и записей выдачи
* Массовое создание, обновление, удаление
* Фильтрация списков через параметры запроса
* Кеширование GET-запросов
* Админ-панель Django

## Эндпоинты

GET, POST, PUT, PATCH, DELETE - для каждого ресурса по стандартным URL:
/api/v1/{resource}/
или
/api/v1/{resource}/{id}/

Массовое удаление: DELETE /api/v1/{resource}/batch/?ids=1,2,3