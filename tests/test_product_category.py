import sys
from io import StringIO

import pytest

from src.product_category import Category, Product, Smartphone, LawnGrass


def test_products_category(product_category) -> None:
    product = product_category._Category__products[0]
    product1 = product_category._Category__products[1]
    product2 = product_category._Category__products[2]
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product1.name == "Iphone 15"
    assert product2.name == "Xiaomi Redmi Note 11"
    assert product_category.name == "Смартфоны"


def test_new_price(product_category) -> None:
    product = product_category._Category__products[0]
    product1 = product_category._Category__products[1]
    product2 = product_category._Category__products[2]
    assert product.price == 180000.0
    assert product1.price == 210000.0
    assert product2.price == 31000.0


def test_add_new_product(product_category) -> None:
    new_info = {
        "name": "Xiaomi Redmi Note 11",
        "description": "1024GB, Синий",
        "price": 31000.0,
        "quantity": 14,
    }
    new_product = Product.new_product(new_info)
    assert new_product.name == "Xiaomi Redmi Note 11"


def test_update_existing_product(product_category) -> None:
    existing_info = {
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 170000.0,
        "quantity": 2,
    }
    updated_product = Product.new_product(existing_info)
    assert updated_product.quantity == 2
    assert updated_product.price == 170000.0


def test_add(product_category) -> None:
    assert (
                   (
                           product_category._Category__products[0].price
                           * product_category._Category__products[0].quantity
                   )
                   + (
                           product_category._Category__products[2].price
                           * product_category._Category__products[2].quantity
                   )
           ) == 1334000
    assert (
                   (
                           product_category._Category__products[1].price
                           * product_category._Category__products[1].quantity
                   )
                   + (
                           product_category._Category__products[2].price
                           * product_category._Category__products[2].quantity
                   )
           ) == 2114000
    assert (
                   (
                           product_category._Category__products[0].price
                           * product_category._Category__products[0].quantity
                   )
                   + (
                           product_category._Category__products[1].price
                           * product_category._Category__products[1].quantity
                   )
           ) == 2580000


def test_str(product_category) -> None:
    product = str(product_category._Category__products[0])
    product1 = str(product_category._Category__products[1])
    product2 = str(product_category._Category__products[2])
    assert product == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."
    assert product1 == "Iphone 15, 210000.0 руб. Остаток: 8 шт."
    assert product2 == "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт."


def test_add_same_products(product_category) -> None:
    product = product_category._Category__products[0]
    product1 = product_category._Category__products[1]
    product2 = product_category._Category__products[2]

    result_1 = product + product1
    result_2 = product + product2
    result_3 = product1 + product2
    assert result_1 == 2580000.0
    assert result_2 == 1334000.0
    assert result_3 == 2114000.0


def test_add_non_product_raises_error() -> None:
    category = Category("Газон", "Газон новый свежий", [])

    test_cases = [
        ("строка", str),
        (123, int),
        (3.14, float),
        ([1, 2, 3], list),
        ({"key": "value"}, dict),
        (None, type(None)),
        (True, bool),
    ]

    for value, expected_type in test_cases:
        with pytest.raises(TypeError) as exc_info:
            category.add_product(value)

        assert "Можно добавлять только объекты Product" in str(exc_info.value)
        assert expected_type.__name__ in str(exc_info.value)


def test_category_add_product_type_error():
    category = Category("Категория", "Описание", [])

    with pytest.raises(TypeError) as exc_info:
        category.add_product("не продукт")

    assert "Можно добавлять только объекты Product" in str(exc_info.value)

def test_product_price_property():
    product = Product("Тест", "Описание", 100.0, 5)
    product.price = -50
    product.price = 0
    assert product.price == 100.0
    assert product.price == 100.0
    assert product.price == 100.0


def test_product_price_decrease_with_confirmation():
    product = Product("Тест", "Описание", 100.0, 5)

    sys.stdin = StringIO('y\n')
    product.price = 80.0
    assert product.price == 80.0

    product = Product("Тест", "Описание", 100.0, 5)
    sys.stdin = StringIO('n\n')
    product.price = 80.0
    assert product.price == 100.0


def test_category_creation():
    product1 = Product("Товар1", "Описание1", 100.0, 5)
    product2 = Product("Товар2", "Описание2", 200.0, 3)

    category = Category("Электроника", "Технические товары", [product1, product2])

    assert category.name == "Электроника"
    assert category.description == "Технические товары"
    assert len(category._Category__products) == 2
    assert Category.category_count > 0
    assert Category.product_count >= 2


def test_lawn_grass_creation():
    grass = LawnGrass(
        name="Трава газонная",
        description="Высококачественная трава",
        price=50.0,
        quantity=100,
        country="Россия",
        germination_period="14 дней",
        color="Зеленый"
    )

    assert grass.name == "Трава газонная"
    assert grass.price == 50.0
    assert grass.country == "Россия"
    assert grass.germination_period == "14 дней"
    assert grass.color == "Зеленый"
    assert isinstance(grass, Product)



def test_product_inheritance_in_category():
    category = Category("Техника", "Описание", [])

    smartphone = Smartphone(
        name="Samsung",
        description="Смартфон",
        price=800.0,
        quantity=3,
        efficiency="Средняя",
        model="Galaxy S23",
        memory="128GB",
        color="White"
    )

    grass = LawnGrass(
        name="Трава",
        description="Газонная",
        price=30.0,
        quantity=50,
        country="Россия",
        germination_period="10 дней",
        color="Зеленый"
    )


    category.add_product(smartphone)
    category.add_product(grass)

    assert len(category._Category__products) == 2
