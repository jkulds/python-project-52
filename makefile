lint:
	poetry run flake8 task_manager

test:
	poetry run python3 manage.py test

test-coverage:
	poetry run coverage run manage.py test
	poetry run coverage report -m --include=task_manager/* --omit=task_manager/settings.py
	poetry run coverage xml --include=task_manager/* --omit=task_manager/settings.py

install:
	poetry install

selfcheck:
	poetry check

check: selfcheck test-coverage lint

dev:
	poetry run python manage.py runserver 5000

migrate:
	poetry run python manage.py makemigrations task_manager
	poetry run python manage.py migrate

PORT ?= 8000
start:
	poetry run gunicorn -w 5 -b 0.0.0.0:5000 task_manager.wsgi

shell:
	poetry run python manage.py shell_plus --ipython

makemessages:
	poetry run python manage.py makemessages --ignore="static" --ignore=".env" -l ru

compilemessages:
	poetry run python manage.py compilemessages