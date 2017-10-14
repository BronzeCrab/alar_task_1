## Задание

I. Python/Flask приложение редактирования списка пользователей:

а) Минимум две страницы: логин и, собственно, список. 
б) Возможность добавлять/удалять/редактировать пользователей и их права: полные (редактирование/добавление/удаление) и только просмотр. 
в) Пользоваться можно только залогинившись и должно действовать ограничение прав. 
г) HTML с запросами через Ajax REST c JSON (простейшее JavaScript приложение - нативно или максимум jQuery) на фронтенде. Да, это не backend, но хороший разработчик должен кристально ясно понимать, что происходит на фронте. 
д) Обязательно использовать SQLAlchemy. Сама база данных - любая RDBMS, но предпочтительно для простоты MySQL или PostgreSQL. 
е) Сид базы - первый пользователь с полными правами.

## Как запустить:
	pip3 insatll -r requirements.txt
	export FLASK_APP=app.py
	flask run