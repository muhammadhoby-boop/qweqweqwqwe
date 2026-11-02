# Todo App

Учебный проект по курсу «Введение в программную инженерию».
Простой консольный менеджер задач на Python.

## Возможности
- Добавление задач
- Просмотр списка задач
- Отметка задачи как выполненной
- Удаление задач
- Сохранение данных в `tasks.json`

## Запуск
```bash
python src/main.py add "Сделать лабораторную"
python src/main.py list
python src/main.py done 1
python src/main.py delete 1
```

## Тесты
```bash
python -m unittest discover tests
```

## Структура
```
todo-app/
├── src/
│   ├── main.py      # CLI
│   └── tasks.py     # логика
├── tests/
│   └── test_tasks.py
├── README.md
├── LICENSE
└── .gitignore
```

## Автор
Гайратов Бобур
