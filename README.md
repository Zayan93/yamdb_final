# yamdb_final

Проект «YaMDb»

Автор: Заян Дандляев

Публичный IP сервера проекта: 51.250.19.48/admin


Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:\
`git clone https://github.com/Zayan93/yamdb_final.git`

Cоздать и активировать виртуальное окружение:\
`python3 -m venv env` \
`source venv/bin/activate`

Установить зависимости из файла requirements.txt:
`python3 -m pip install --upgrade pip` \
`pip install -r requirements.txt`

Выполнить миграции:\
`python3 manage.py migrate` \
`python3 manage.py makemigrations`



Запустить проект:\
`python3 manage.py runserver` 

Более подробная документация о проекте:\
`http://127.0.0.1:8000/redoc/`


![status](https://github.com/Zayan93/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)
