Конечно! Вот примеры использования модулей `os`, `sys`, `collections`, `itertools`, `functools`, `datetime` и `random` в Python:

### Модуль `os`

Модуль `os` предоставляет функции для взаимодействия с операционной системой.

```python
import os

# Получение текущего рабочего каталога
current_directory = os.getcwd()
print(f"Current Directory: {current_directory}")

# Создание нового каталога
os.mkdir('new_directory')

# Переименование файла или каталога
os.rename('new_directory', 'renamed_directory')

# Удаление файла или каталога
os.rmdir('renamed_directory')
```

### Модуль `sys`

Модуль `sys` предоставляет доступ к некоторым переменным, используемым или поддерживаемым интерпретатором Python.

```python
import sys

# Получение аргументов командной строки
arguments = sys.argv
print(f"Arguments: {arguments}")

# Завершение программы с кодом выхода
sys.exit(0)

# Получение информации о платформе
platform_info = sys.platform
print(f"Platform: {platform_info}")
```

### Модуль `collections`

Модуль `collections` предоставляет специализированные контейнеры данных.

```python
from collections import Counter, defaultdict, deque, namedtuple

# Counter: Подсчет элементов
counter = Counter(['apple', 'banana', 'apple', 'orange', 'banana', 'apple'])
print(counter)

# defaultdict: Словарь с значениями по умолчанию
default_dict = defaultdict(int)
default_dict['apple'] += 1
print(default_dict)

# deque: Двухсторонняя очередь
d = deque(['apple', 'banana', 'orange'])
d.append('grape')
d.appendleft('cherry')
print(d)

# namedtuple: Именованный кортеж
Point = namedtuple('Point', 'x y')
p = Point(10, 20)
print(p)
print(p.x, p.y)
```

### Модуль `itertools`

Модуль `itertools` предоставляет функции для создания итераторов для эффективных циклов.

```python
import itertools

# count: Бесконечный счетчик
for i in itertools.count(10, 2):
    if i > 20:
        break
    print(i)

# cycle: Повторение элементов
for i, elem in enumerate(itertools.cycle(['apple', 'banana', 'orange'])):
    if i > 5:
        break
    print(elem)

# chain: Объединение нескольких итераторов
combined = list(itertools.chain([1, 2, 3], ['a', 'b', 'c']))
print(combined)

# combinations: Комбинации элементов
combinations = list(itertools.combinations(['a', 'b', 'c'], 2))
print(combinations)
```

### Модуль `functools`

Модуль `functools` предоставляет функции высшего порядка.

```python
from functools import lru_cache, partial, reduce

# lru_cache: Кэширование результатов функции
@lru_cache(maxsize=32)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print([fibonacci(n) for n in range(10)])

# partial: Частичное применение аргументов функции
def multiply(x, y):
    return x * y

double = partial(multiply, 2)
print(double(5))

# reduce: Свертка функции
numbers = [1, 2, 3, 4, 5]
result = reduce(lambda x, y: x + y, numbers)
print(result)
```

### Модуль `datetime`

Модуль `datetime` предоставляет классы для работы с датой и временем.

```python
from datetime import date, datetime, timedelta

# Текущая дата и время
now = datetime.now()
print(f"Current DateTime: {now}")

# Создание объекта даты
today = date.today()
print(f"Today's Date: {today}")

# Добавление и вычитание времени
tomorrow = today + timedelta(days=1)
print(f"Tomorrow's Date: {tomorrow}")

# Форматирование даты
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print(f"Formatted DateTime: {formatted_date}")
```

### Модуль `random`

Модуль `random` предоставляет функции для генерации случайных чисел.

```python
import random

# Случайное целое число в диапазоне
rand_int = random.randint(1, 10)
print(f"Random Integer: {rand_int}")

# Случайный элемент из списка
fruits = ['apple', 'banana', 'orange', 'grape', 'cherry']
rand_fruit = random.choice(fruits)
print(f"Random Fruit: {rand_fruit}")

# Перемешивание списка
random.shuffle(fruits)
print(f"Shuffled Fruits: {fruits}")

# Случайное число с плавающей запятой
rand_float = random.uniform(1.0, 10.0)
print(f"Random Float: {rand_float}")
```

### Другие полезные модули

**Модуль `math`**: Предоставляет математические функции.

```python
import math

# Вычисление квадратного корня
sqrt_value = math.sqrt(16)
print(f"Square Root: {sqrt_value}")

# Вычисление синуса угла в радианах
sin_value = math.sin(math.pi / 2)
print(f"Sine: {sin_value}")
```

**Модуль `json`**: Работа с JSON данными.

```python
import json

# Преобразование словаря в JSON строку
data = {'name': 'John', 'age': 30, 'city': 'New York'}
json_data = json.dumps(data)
print(f"JSON Data: {json_data}")

# Преобразование JSON строки в словарь
data_dict = json.loads(json_data)
print(f"Dictionary: {data_dict}")
```

Эти примеры показывают, как можно использовать различные модули Python для решения различных задач и расширения функциональности ваших программ.