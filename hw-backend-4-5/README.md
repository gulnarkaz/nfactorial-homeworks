# books

Данная папка предназначена для следующих заданий:
- books-read
- books-create
- books-update
- books-delete


> 💡 Необходимо чтобы задания были выполнены в данной папке.

## Запуск проекта

Установить зависимости:

```bash
poetry install
```

Войти в окружение poetry:

```bash
poetry shell
```

Запустить FastAPI-приложение.

```bash
uvicorn app.main:app --reload
```

После этого сервер запуститься на порту 8000. Чтобы проверить подключение сделайте запрос на [localhost:8000](http://localhost:8000).

```bash
curl localhost:8000
```

Запустить тесты.

```bash
pytest -v
```

## 1. books-read

В этом задании реализуем `READ` операции над сущностью - "книга".

### Задание

- Реализовать обработчик для маршрута `GET /books`, который отображает список книг.
    - Должен принимать параметр запроса `page`, который отвечает за номер страницы
    - Если параметр в запросе не указан, то по дефолту показывать первую страницу
    - Должен выводить по 10 элементов на каждой странице
- Создать шаблон для `GET /books`
    - Выводить в цикле каждую книгу со ссылкой на нее `/books/{id}`. В качестве текста ссылки использовать поле `title`.
    - Переключение между страницами сделать через кнопки "вперед" и "назад".
        - Если страница первая, то не показывать "назад".
        - Если страница последняя, то не показывать "вперед".
- Реализовать обработчик для маршрута `GET /books/{id}`, который отображает детальную информацию о книге.
    - Если книга не найдена, то вернуть текст `Not Found` с кодом 404.
- Создать шаблона для `GET /books/{id}`.
    - Вывести всю доступную информацию о книге.

### Подсказки

- Переход между страницами реализуется с помощью параметра запроса `?page=`
- [If Expresion](https://jinja.palletsprojects.com/en/3.1.x/templates/#whitespace-control)

## 2. books-create

В этом задании вам предстоит попрактиковаться над `CREATE` операцией в `CRUD`.

### Задание

- Реализовать обработчик для маршрута `GET /books/new`, который отображает форму создания книги
- Создать шаблон для `GET /books/new`, который принимает поля
    - `title` – название
    - `author` – автор
    - `year` – год издания
    - `total_pages` – количество страниц
    - `genre` – жанр
- Реализовать обработчик для маршрута `POST /books` для создания книги

### Подсказки
Для сохранения использовать метод save()

## 3. books-update

### Задание

- Реализовать форму `GET /books/{id}/edit`
    - Подтягивает существущие данные и вставляет в форму
    - Если книги нет, то вернуть `Not Found`, 404
- Реализовать обработчик `POST /books/{id}/edit`
    - Обновляет данные книги
    - Если книги нет, то вернуть `Not Found`, 404
    - Если успешно обновил, то перенаправляет на `GET /books/{id}`

    ## 4. books-delete

### Задание

- Добавить форму удаления в шаблоне на `GET /books/{id}`
- Реализовать обработчик `POST /books/{id}/delete`
    - Удаляет книгу
    - Перенаправляет на страницу со списком книг