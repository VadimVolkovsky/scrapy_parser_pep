### Асинхронный парсер PEP

Парсер работает на асинхронном фреймворке Scrapy 

Список поддерживаемых сайтов:

https://peps.python.org/

### Инструкция по запуску:
**Клонируйте репозиторий:**
```
git clone git@github.com:VadimVolkovsky/scrapy_parser_pep.git
```

**Установите и активируйте виртуальное окружение:**
для MacOS:
```
python3 -m venv venv
```

для Windows:
```
python -m venv venv
source venv/bin/activate
source venv/Scripts/activate
```
**Установите зависимости из файла requirements.txt:**
```
pip install -r requirements.txt
```

**Из корневой директории запустите парсер:**
```
scrapy crawl pep
```

**Вывод результатов в файл:**
Результаты парсинга сохраняются в папке results в формате csv-файлов.

- Файл "pep_<дата сохранения>.csv" содержит информацию о номерах, названиях и статусах полученных PEP.

- Файл "status_summary_<дата сохранения>.csv" содержит информацию о полученных статусах PEP, о количестве PEP с каждым статусом и общее количество PEP.

**Технологии:**
- Python 3.9
- Scrapy

### Автор проекта:

Vadim Volkovsky
