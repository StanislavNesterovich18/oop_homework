import pytest

from src.product_category import Category, Product


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
    assert result_1 == 13
    assert result_2 == 19
    assert result_3 == 22


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
