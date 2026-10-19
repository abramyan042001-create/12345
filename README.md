# Книжная полка

Учебный проект на Django: каталог книг, авторов и издательств. В проекте используются представления на основе классов (CBV), а автор и издательство связаны с книгой через `ForeignKey`.

## Возможности

- список книг с поиском по названию, автору и издательству;
- карточка книги с информацией об авторе и издательстве;
- создание, редактирование и удаление книги;
- страницы справочников авторов и издательств;
- Django Admin для управления всеми данными;
- SQLite, адаптивная русскоязычная вёрстка.

## Запуск

Требуется Python 3.10+.

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Откройте http://127.0.0.1:8000/ . Для добавления авторов и издательств войдите в админ-панель по адресу http://127.0.0.1:8000/admin/ . После этого их можно выбирать в форме создания книги.

## Структура данных

- `Author`: имя и биография;
- `Publisher`: название и город;
- `Book`: название, год, описание, `ForeignKey` на автора и издательство.

## Основные CBV

- `BookListView` — список и поиск книг;
- `BookDetailView` — карточка книги;
- `BookCreateView`, `BookUpdateView`, `BookDeleteView` — создание, изменение и удаление;
- `AuthorListView`, `PublisherListView` — справочники.

## Проверки

```bash
python manage.py test
```
