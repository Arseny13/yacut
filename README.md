# service_YaCut

<h4>Автор:</h4>

**Изимов Арсений**  - студент Яндекс.Практикума Когорта 16+
https://github.com/Arseny13


<h2>Техническое описание проекта</h2>
На большинстве сайтов адреса страниц довольно длинные, например, как у той страницы, на которой вы сейчас находитесь. Делиться такими длинными ссылками не всегда удобно, а иногда и вовсе невозможно. 

Проект YaCut — это сервис укорачивания ссылок. Его назначение — ассоциировать длинную пользовательскую ссылку с короткой, которую предлагает сам пользователь или предоставляет сервис.

<h2>Задание</h2>

Ваша задача — написать сервис укорачивания ссылок и API к нему. 
Ключевые возможности сервиса:
- генерация коротких ссылок и связь их с исходными длинными ссылками,
- переадресация на исходный адрес при обращении к коротким ссылкам.
Пользовательский интерфейс сервиса — одна страница с формой. Эта форма должна состоять из двух полей:
- обязательного для длинной исходной ссылки;
- необязательного для пользовательского варианта короткой ссылки.
Пользовательский вариант короткой ссылки не должен превышать 16 символов.

<h2>Используемые технологии</h2>

- alembic==1.7.5
- attrs==21.4.0
- click==8.0.3
- faker==12.0.1;
- flask-migrate==3.1.0
- flask-sqlalchemy==2.5.1
- flask-wtf==1.0.0
- flask==2.0.2
- greenlet
- iniconfig==1.1.1
- itsdangerous==2.0.1
- jinja2==3.0.3
- mako==1.1.6
- markupsafe==2.0.1
- mccabe==0.6.1
- mixer==7.2.2
- packaging==21.3; python_version >= '3.6'
- pluggy==1.0.0; python_version >= '3.6'
- py==1.11.0; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3, 3.4'
- pycodestyle==2.8.0; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3, 3.4'
- pyflakes==2.4.0; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3'
- pyparsing==3.0.7; python_version >= '3.6'
- pytest-env==0.6.2
- pytest==7.1.1
- python-dateutil==2.8.2; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3'
- python-dotenv==0.19.2
- six==1.16.0; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3'
- sqlalchemy==1.4.29
- tomli==2.0.1; python_version >= '3.7'
- werkzeug==2.0.2
- wtforms==3.0.1


<h2>Как использовать</h2>

Клонировать репозиторий и перейти в него в командной строке:

```
git clone 
```

```
cd yacut
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```
