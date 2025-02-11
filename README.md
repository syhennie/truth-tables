# Проект: Решение задач по построению таблиц истинности

## Описание

Этот проект содержит решение трёх задач по построению таблиц истинности для логических выражений.

### Задача 1: Таблица истинности для выражения с тремя переменными

**Описание**:
Первая задача заключается в построении таблицы истинности для сложного логического выражения, состоящего из трёх переменных: `a`, `b` и `c`.

**Формат ввода**:
Вводится логическое выражение, валидное для языка Python, в котором используются три переменные `a`, `b`, `c` и стандартные логические операторы Python (`and`, `or`, `not`).

**Формат вывода**:
Программа выводит таблицу истинности для всех возможных комбинаций значений переменных `a`, `b`, `c` и результат выражения.

### Задача 2: Таблица истинности для выражения с произвольным количеством переменных

**Описание**:
Вторая задача расширяет первую, предоставляя возможность построения таблицы истинности для логических выражений с произвольным количеством переменных.

**Формат ввода**:
Вводится логическое выражение с использованием переменных, валидное для Python.

**Формат вывода**:
Программа выводит таблицу истинности для всех возможных комбинаций значений всех переменных, присутствующих в выражении, и результат выражения.

### Задача 3: Таблица истинности с нестандартными логическими операциями

**Описание**:
Третья задача добавляет поддержку нестандартных логических операций, которые не реализованы в Python по умолчанию:
- Импликация (`->`)
- Строгая дизъюнкция (`^`)
- Эквивалентность (`~`)

**Формат ввода**:
Вводится логическое выражение, которое может содержать переменные, стандартные логические операторы Python (`and`, `or`, `not`), а также нестандартные операции (`->`, `^`, `~`).

**Формат вывода**:
Программа строит таблицу истинности для всех возможных комбинаций переменных и вычисляет результат выражения, учитывая нестандартные логические операции.

## Структура проекта

- `truth-table-1.py`: решение задачи 1
- `thuth-table-2.py`: решение задачи 2
- `truth-table-3.py`: решение задачи 3

