Для собеседования на позицию Python middle-разработчика потребуется более глубокое понимание языка и экосистемы, а также способность решать более сложные задачи. Вот список вопросов, которые могут помочь вам подготовиться:

### 1. Глубокое понимание языка Python

**Вопросы по основам языка:**

1. **Какая разница между `deepcopy` и `copy` в Python?**
   - `copy` создает поверхностную копию объекта, а `deepcopy` создает глубокую копию, включая все вложенные объекты.

2. **Как работают декораторы и как их использовать?**
   ```python
   def my_decorator(func):
       def wrapper():
           print("Something is happening before the function is called.")
           func()
           print("Something is happening after the function is called.")
       return wrapper

   @my_decorator
   def say_hello():
       print("Hello!")

   say_hello()
   ```

3. **Что такое генераторы и как их использовать?**
   - Генераторы позволяют создавать итераторы с помощью функции и ключевого слова `yield`.

   ```python
   def my_generator():
       yield 1
       yield 2
       yield 3

   for value in my_generator():
       print(value)
   ```

### 2. Взаимодействие с данными

**Работа с базами данных:**

1. **Как подключиться к базе данных PostgreSQL с использованием SQLAlchemy?**
   ```python
   from sqlalchemy import create_engine

   engine = create_engine('postgresql://user:password@localhost/dbname')
   ```

2. **Как использовать ORM для работы с базой данных?**
   ```python
   from sqlalchemy import Column, Integer, String, create_engine
   from sqlalchemy.ext.declarative import declarative_base
   from sqlalchemy.orm import sessionmaker

   Base = declarative_base()

   class User(Base):
       __tablename__ = 'users'
       id = Column(Integer, primary_key=True)
       name = Column(String)
       age = Column(Integer)

   engine = create_engine('sqlite:///users.db')
   Base.metadata.create_all(engine)

   Session = sessionmaker(bind=engine)
   session = Session()

   new_user = User(name='John', age=30)
   session.add(new_user)
   session.commit()
   ```

### 3. Объектно-ориентированное программирование (ООП)

1. **Что такое полиморфизм и как его использовать в Python?**
   - Полиморфизм позволяет использовать одно и то же имя метода для разных типов данных.

   ```python
   class Animal:
       def speak(self):
           pass

   class Dog(Animal):
       def speak(self):
           return "Woof!"

   class Cat(Animal):
       def speak(self):
           return "Meow!"

   animals = [Dog(), Cat()]
   for animal in animals:
       print(animal.speak())
   ```

2. **Что такое метаклассы и как их использовать?**
   - Метаклассы — это классы для создания классов. Они позволяют изменять поведение классов.

   ```python
   class Meta(type):
       def __new__(cls, name, bases, dct):
           print(f"Creating class {name}")
           return super().__new__(cls, name, bases, dct)

   class MyClass(metaclass=Meta):
       pass
   ```

### 4. Асинхронное программирование

1. **Что такое `asyncio` и как его использовать для создания асинхронных задач?**
   ```python
   import asyncio

   async def main():
       print('Hello ...')
       await asyncio.sleep(1)
       print('... World!')

   asyncio.run(main())
   ```

2. **Как работают `async` и `await`?**
   - `async` используется для определения асинхронной функции, а `await` для ожидания завершения корутины.

### 5. Тестирование

1. **Как писать юнит-тесты с использованием библиотеки `unittest`?**
   ```python
   import unittest

   def add(a, b):
       return a + b

   class TestMath(unittest.TestCase):
       def test_add(self):
           self.assertEqual(add(1, 2), 3)

   if __name__ == '__main__':
       unittest.main()
   ```

2. **Как использовать библиотеку `pytest`?**
   ```python
   def add(a, b):
       return a + b

   def test_add():
       assert add(1, 2) == 3
   ```

### 6. Веб-разработка

1. **Как работает Django ORM?**
   - Django ORM позволяет взаимодействовать с базой данных через Python-классы и методы.

   ```python
   from django.db import models

   class User(models.Model):
       name = models.CharField(max_length=100)
       age = models.IntegerField()

   users = User.objects.filter(age__gt=20)
   ```

2. **Как создавать API с использованием Django REST Framework?**
   ```python
   from rest_framework import serializers, viewsets
   from .models import User

   class UserSerializer(serializers.ModelSerializer):
       class Meta:
           model = User
           fields = '__all__'

   class UserViewSet(viewsets.ModelViewSet):
       queryset = User.objects.all()
       serializer_class = UserSerializer
   ```

### 7. Алгоритмы и структуры данных

1. **Как реализовать двоичный поиск?**
   ```python
   def binary_search(arr, target):
       left, right = 0, len(arr) - 1
       while left <= right:
           mid = (left + right) // 2
           if arr[mid] == target:
               return mid
           elif arr[mid] < target:
               left = mid + 1
           else:
               right = mid - 1
       return -1
   ```

2. **Как реализовать связанный список?**
   ```python
   class Node:
       def __init__(self, data):
           self.data = data
           self.next = None

   class LinkedList:
       def __init__(self):
           self.head = None

       def append(self, data):
           if not self.head:
               self.head = Node(data)
               return
           current = self.head
           while current.next:
               current = current.next
           current.next = Node(data)
   ```

### 8. Оптимизация и производительность

1. **Как профилировать код в Python?**
   - Использовать модуль `cProfile`.

   ```python
   import cProfile

   def my_function():
       # Код для профилирования
       pass

   cProfile.run('my_function()')
   ```

2. **Как работать с памятью в Python?**
   - Использовать модуль `memory_profiler`.

   ```python
   from memory_profiler import profile

   @profile
   def my_function():
       a = [1] * (10**6)
       b = [2] * (2 * 10**7)
       del b
       return a

   my_function()
   ```

### 9. Работа с API

1. **Как отправить GET-запрос с использованием библиотеки `requests`?**
   ```python
   import requests

   response = requests.get('https://api.example.com/data')
   print(response.json())
   ```

2. **Как обработать JSON-ответ от API?**
   ```python
   import requests

   response = requests.get('https://api.example.com/data')
   data = response.json()
   print(data)
   ```

### 10. DevOps и контейнеризация

1. **Как создать Dockerfile для Python-приложения?**
   ```dockerfile
   FROM python:3.8-slim-buster

   WORKDIR /app

   COPY requirements.txt requirements.txt
   RUN pip install -r requirements.txt

   COPY . .

   CMD ["python", "app.py"]
   ```

2. **Как использовать Docker Compose для оркестрации контейнеров?**
   ```yaml
   version: '3.8'

   services:
     web:
       build: .
       ports:
         - "5000:5000"
       volumes:
         - .:/app
       depends_on:
         - db

     db:
       image: postgres
       environment:
         POSTGRES_USER: user
         POSTGRES_PASSWORD: password
         POSTGRES_DB: mydb
   ```

### Практические задачи

1. **Напишите функцию для вычисления n-го числа Фибоначчи с помощью рекурсии и итерации.**
   ```python
   def fibonacci_recursive(n):
       if n <= 1:
           return n
       else:
           return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

   def fibonacci_iterative(n):
       a, b = 0, 1
       for _ in range(n):
           a, b = b, a + b
       return a
   ```

2. **Напишите функцию для проверки, является ли строка анаграммой другой строки.**
   ```python
   def is_anagram(str1, str2):
       return sorted(str1) == sorted(str2)
   ```

Подготовка к этим вопросам поможет вам успешно пройти собеседование на позицию Python middle-разработчика. Удачи!