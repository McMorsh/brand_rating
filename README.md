# Brand Rating

Скрипт для анализа рейтингов товаров по брендам.  
Обрабатывает один или несколько CSV-файлов и формирует отчёт **average-rating** - средний рейтинг по каждому бренду.

---

## Возможности

- Проект принимает csv файлы через параметр `--files` или `-f`
- Формирует нужный отчет через параметр `--report` или `-r`
- Отчет выводится в консоли с помощью библиотеки `tabulate`
- Доступно свободное расширение видов отчетов

---

## Расширение функционала

1. Создать свой класс и унаследовать базовый класс `Report`
2. Переопределить методы `generate` и `display`
3. Добавить класс в словарь `REPORTS`

Пример:

```python
class AveragePriceReport(Report):
    name = "average-price"
    ...


REPORTS = {
    "average-rating": RatingReport,
}
```

---

## Структура проекта

```
brand_rating/
│
├── brand_analyzer/ 
│   ├── __init__.py
│   ├── io.py             # Чтение CSV-файлов
│   ├── analyzer.py       # Реализация отчётов
│   └── cli.py            # Command Line Interface
│
├── tests/
│   ├── __init__.py
│   ├── test_command_line_interface.py
│   ├── test_input_output.py
│   └── test_analyzer.py
│
├── data/
│   └── data_maker.py   # Вспомогательный код для создания таблиц
├── main.py     # Точка запуска
├── requirements.txt
└── README.md
```

---

## Тестирование

Запуск тестов с помощью Pytest:

```bash
pytest -v
```

---

## Примеры запуска

### Пример 1.

```bash
python main.py --files data/test_data_1.csv data/test_data_2.csv --report average-rating
```

test_data_1.csv:

```csv
name,brand,price,rating
iphone 15,apple,399,4.9
ipod,apple,150,4.2
galaxy S99,samsung,1199,4.8
```

test_data_2.csv:

```csv
name,brand,price,rating
redmi note 12 pro max ultra,xiaomi,199,4.3
galaxy j7,samsung,50,4.1
```

Результат:

```
+----+---------+----------+
|    | brand   |   rating |
|----+---------+----------|
|  1 | Apple   |     4.55 |
|  2 | Samsung |     4.45 |
|  3 | Xiaomi  |     4.3  |
+----+---------+----------+
```

### Пример 2.

```bash
python main.py --files data/products1.csv data/products2.csv --report average-rating    
```

products1.csv:

```csv
name,brand,price,rating
iphone 15 pro,apple,999,4.9
galaxy s23 ultra,samsung,1199,4.8
redmi note 12,xiaomi,199,4.6
iphone 14,apple,799,4.7
galaxy a54,samsung,349,4.2

```

products2.csv:

```csv
poco x5 pro,xiaomi,299,4.4
iphone se,apple,429,4.1
galaxy z flip 5,samsung,999,4.6
redmi 10c,xiaomi,149,4.1
iphone 13 mini,apple,599,4.5
```

Результат:

```
+----+---------+----------+
|    | brand   |   rating |
|----+---------+----------|
|  1 | Apple   |     4.55 |
|  2 | Samsung |     4.53 |
|  3 | Xiaomi  |     4.37 |
+----+---------+----------+
```

### Пример 3.

```bash
python main.py --f data/test_data_invalid.csv --r average-rating 
```

test_data_invalid.csv:

```csv
name,brand,price,rating
iphone 15,apple,399,bad
galaxy S99,samsung,,4.8
pixel 8,google,299,
```

Результат:

```
+----+---------+----------+
|    | brand   |   rating |
|----+---------+----------|
|  1 | Samsung |      4.8 |
+----+---------+----------+
```

---

## Установка

```bash
git clone https://github.com/McMorsh/brand_rating.git
cd brand_rating
pip install -r requirements.txt
```

