# Учебный проект по Python

Анализатор финансовых транзакций: загружает данные из Excel-файла, фильтрует и группирует операции, строит отчёты.

---

## Реализация функций

1. `class Product`   
   Шаблон для класса Product определяющий следующие свойства: название (name),
описание (description),цена (price),количество в наличии (quantity).
2. `class Category`  
Шаблон для класса Category определяющий следующие свойства: название (name),
описание (description),список товаров категории (products).
## Структура проекта

```bash
├── data                    
├── htmlcov
├──src
│   ├── __init__.py     
│   ├── product_category.py 
├── tests/                    # Pytest-тесты
│   ├── __init__.py
│   ├──conftest.py           # конфигурация для тестов
│   ├── test_product_category.py
├── .coverage
├── .flake8
├── .gitignore
├── config.py
├── main.py
├── poetry.lock
├── pyproject.toml
├── README.md                 # Описание проекта
```

## Тестирование

Запуск тестов осуществляется через команду pytest.

- `test_product_category.py` тестирование классов
## Используемые технологии

- Python 3.13
- pytest
- pip

### Документация

Более подробную документацию по каждой функции можно найти в `docstrings` внутри исходного кода.

### Лицензия

Сведения о лицензии проекта (например, MIT, Apache 2.0) [укажите здесь](https://github.com).