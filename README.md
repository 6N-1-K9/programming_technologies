# PTLab1 — Лабораторная работа №1

Проект расчёта среднего рейтинга студентов по дисциплинам
с поддержкой форматов TXT и YAML.

## Вариант 1
Формат входного файла: YAML.
Расчётная процедура: подсчёт количества студентов-отличников
(все баллы >= 90).

## Установка

python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

## Запуск

PYTHONPATH=./src python src/main.py -p data/data.yaml

## Тестирование

PYTHONPATH=./src pytest test
pycodestyle src test
