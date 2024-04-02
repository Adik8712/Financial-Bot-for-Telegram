# Финансовый Бот для Telegram

Этот проект представляет собой Telegram бота, разработанного для помощи пользователю в освоении финансовой грамотности. Бот позволяет учитывать расходы и доходы, а также предоставляет возможность просмотра графиков доходов и расходов.

## Установка

1. Сначала склонируй репозиторий:

```bash
git clone https://github.com/Adik8712/Financial-Bot-for-Telegram.git
```

2. Перейди в каталог проекта:

```bash
cd Financial-Bot-for-Telegram
```

3. Установи зависимости:

```bash
pip install -r requirements.txt
```

4. Создай файл `config.ini` и добавь туда следующие настройки:

```ini
[Telegram]
TOKEN_KEY = 'your_telegram_bot_token'
```

5. Запусти бота:

```bash
python manage.py runserver
```

## Функциональность

Этот бот предоставляет ряд полезных функций:

- Добавление доходов с указанием категории и комментария.
- Добавление расходов с указанием категории и комментария.
- Просмотр статистики доходов и расходов.
- Построение графиков для визуализации доходов и расходов.

## Технологии

Проект использует следующие технологии:

- Django - для создания веб-приложения.
- pyTelegramBotAPI - для взаимодействия с API Telegram.

## Структура проекта

У данного проекта вот такая структура:

```

.
├── config.ini
├── db.sqlite3
├── LICENSE
├── main
│   ├── admin.py
│   ├── apps.py
│   ├── bot.py
│   ├── __init__.py
│   ├── keyboards
│   │   ├── buttons.py
│   │   ├── inlines.py
│   │   └── __pycache__
│   ├── management
│   │   └── commands
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── 0002_telegramuserincome.py
│   │   ├── 0003_telegramsupport.py
│   │   ├── 0004_telegramanswers.py
│   │   ├── 0005_telegramexpense.py
│   │   ├── 0006_telegramuser_chart_income_alter_telegramuser_chart.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   ├── models.py
│   ├── __pycache__
│   │   ├── admin.cpython-311.pyc
│   │   ├── apps.cpython-311.pyc
│   │   ├── bot.cpython-311.pyc
│   │   ├── __init__.cpython-311.pyc
│   │   ├── models.cpython-311.pyc
│   │   └── signals.cpython-311.pyc
│   ├── signals.py
│   ├── tests.py
│   ├── utils
│   │   ├── chart.py
│   │   ├── __pycache__
│   │   └── utils.py
│   └── views.py
├── main.log
├── manage.py
├── media
│   ├── chart
│   │   ├── 5792605910_bPmg8Vm.png
│   │   └── 5792605910.png
│   └── chart_income
│       └── 5792605910_income.png
├── plaintext.tree
├── README.md
├── requirements.txt
├── TelegramBotProject
│   ├── asgi.py
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-311.pyc
│   │   ├── settings.cpython-311.pyc
│   │   ├── urls.cpython-311.pyc
│   │   └── wsgi.cpython-311.pyc
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── venv
    ├── bin
    │   ├── activate
    │   ├── activate.csh
    │   ├── activate.fish
    │   ├── activate.nu
    │   ├── activate.ps1
    │   ├── activate_this.py
    │   ├── django-admin
    │   ├── f2py
    │   ├── fonttools
    │   ├── normalizer
    │   ├── pip
    │   ├── pip3
    │   ├── pip-3.11
    │   ├── pip3.11
    │   ├── pyftmerge
    │   ├── pyftsubset
    │   ├── python -> /usr/bin/python3
    │   ├── python3 -> python
    │   ├── python3.11 -> python
    │   ├── sqlformat
    │   ├── ttx
    │   ├── wheel
    │   ├── wheel3
    │   ├── wheel-3.11
    │   └── wheel3.11
    ├── lib
    │   └── python3.11
    ├── pyvenv.cfg
    └── share
        └── man

```

## Авторы

Проект создан Адиком. [Профиль GitHub](https://github.com/Adik8712).

## Лицензия

Этот проект распространяется под лицензией MIT License - подробности смотри в файле [LICENSE](LICENSE).