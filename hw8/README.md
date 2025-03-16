<<<<<<< HEAD
# nfactorial-homeworks
All my assignments on backend-Python nfactorial course
=======

В этом задании мы переведем наш API на SQLAlchemy.

По итогу задания у вас должно быть создано 3 миграции (файла):

На создание таблицы пользователей users
На создание таблицы пользователей flowers
На создание таблицы пользователей purchases 💎


Задания
1. signup

Переписать методы UsersRepository на использование sqlalchemy
Адаптировать POST /signup под sqlalchemy (db: Session)

2. login

Адаптировать POST /login под sqlalchemy (db: Session)
Адаптировать GET /profile под sqlalchemy (db: Session)

3. flowers

Адаптировать GET /flowers под sqlalchemy (db: Session)
Адаптировать POST /flowers под sqlalchemy (db: Session)
Реализовать обработчик для изменения объекта PATCH /flowers/{flower_id}
Реализовать обработчик для удаления объекта DELETE /flowers/{flower_id}

4. cart

Адаптировать GET /cart/items под sqlalchemy (db: Session)

5. purchased 💎

Адаптировать POST /purchased под sqlalchemy (db: Session)
Адаптировать GET /purchased под sqlalchemy (db: Session)
>>>>>>> cfd529c (Your commit message)
