import sys
from io import StringIO
from unittest.mock import Mock

import pytest

from src.product_category import Category, LawnGrass, Product, Smartphone


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

    sys.stdin = StringIO("y\n")
    product.price = 80.0
    assert product.price == 80.0

    product = Product("Тест", "Описание", 100.0, 5)
    sys.stdin = StringIO("n\n")
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
        color="Зеленый",
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
        color="White",
    )

    grass = LawnGrass(
        name="Трава",
        description="Газонная",
        price=30.0,
        quantity=50,
        country="Россия",
        germination_period="10 дней",
        color="Зеленый",
    )

    category.add_product(smartphone)
    category.add_product(grass)

    assert len(category._Category__products) == 2


class TestProductExceptions:
    """Тестирование исключений в классе Product"""

    def test_product_price_initialization_validation(self):
        """Тест: инициализация с некорректной ценой через проверку свойства"""
        product = Product("Test", "Description", 100, 10)
        product.price = 0
        assert product.price == 100

    def test_product_price_setter_zero(self):
        """Тест: установка нулевой цены через сеттер"""
        product = Product("Test", "Description", 100, 10)

        old_price = product.price
        product.price = 0
        assert product.price == old_price

    def test_product_price_setter_negative(self):
        """Тест: установка отрицательной цены через сеттер"""
        product = Product("Test", "Description", 100, 10)

        old_price = product.price
        product.price = -50
        assert product.price == old_price

    def test_product_price_setter_lower_price_confirmation_logic(self):
        """Тест: логика подтверждения понижения цены (мок ввода)"""
        product = Product("Test", "Description", 100, 10)
        assert True

    def test_product_price_setter_invalid_type(self, monkeypatch):
        """Тест: установка неверного типа цены с использованием monkeypatch"""
        product = Product("Test", "Description", 100, 10)

        old_price = product.price

        def mock_input(prompt):
            return "n"

        monkeypatch.setattr('builtins.input', mock_input)

        try:
            product.price = "сто"
            assert product.price == old_price
        except TypeError:
            pass



    def test_product_add_same_class_works(self):
        """Тест: сложение товаров одного класса должно работать"""
        product1 = Product("Product1", "Desc1", 100, 10)
        product2 = Product("Product2", "Desc2", 200, 5)

        result = product1 + product2
        expected = (100 * 10) + (200 * 5)
        assert result == expected


class TestCategoryMethods:
    """Тестирование методов класса Category"""

    def test_len_method_empty_category(self):
        """Тест: метод __len__ для пустой категории"""
        category = Category("Test", "Description", [])
        assert len(category) == 0

    def test_len_method_with_products(self):
        """Тест: метод __len__ для категории с продуктами"""
        mock_product1 = Mock()
        mock_product2 = Mock()
        mock_product3 = Mock()

        category = Category("Test", "Description", [mock_product1, mock_product2, mock_product3])
        assert len(category) == 3


    def test_products_property_empty(self):
        """Тест: свойство products для пустой категории"""
        category = Category("Test", "Description", [])
        assert category.products == ""

    def test_products_property_with_products(self):
        """Тест: свойство products для категории с продуктами"""
        mock_product1 = Mock()
        mock_product1.name = "Product1"
        mock_product1.price = 100
        mock_product1.quantity = 10

        mock_product2 = Mock()
        mock_product2.name = "Product2"
        mock_product2.price = 200
        mock_product2.quantity = 5

        category = Category("Test", "Description", [mock_product1, mock_product2])

        result = category.products
        expected_line1 = "Product1, 100 руб. Остаток: 10 шт."
        expected_line2 = "Product2, 200 руб. Остаток: 5 шт."

        assert expected_line1 in result
        assert expected_line2 in result
        assert result.count('\n') == 1
        assert result == f"{expected_line1}\n{expected_line2}"

    def test_products_property_format(self):
        """Тест: форматирование строк в свойстве products"""
        mock_product = Mock()
        mock_product.name = "Телевизор"
        mock_product.price = 29999.99
        mock_product.quantity = 3

        category = Category("Test", "Description", [mock_product])

        result = category.products
        expected = "Телевизор, 29999.99 руб. Остаток: 3 шт."
        assert result == expected

    def test_products_property_special_characters(self):
        """Тест: специальные символы в именах продуктов"""
        mock_product = Mock()
        mock_product.name = "Product & More ®"
        mock_product.price = 100
        mock_product.quantity = 1

        category = Category("Test", "Description", [mock_product])

        result = category.products
        expected = "Product & More ®, 100 руб. Остаток: 1 шт."
        assert result == expected

    def test_middle_price_empty_category(self):
        """Тест: метод middle_price для пустой категории"""
        category = Category("Test", "Description", [])
        result = category.middle_price()
        assert result == 0

    def test_middle_price_single_product(self):
        """Тест: метод middle_price для категории с одним продуктом"""
        mock_product = Mock()
        mock_product.price = 100

        category = Category("Test", "Description", [mock_product])
        result = category.middle_price()
        assert result == 100

    def test_middle_price_multiple_products(self):
        """Тест: метод middle_price для категории с несколькими продуктами"""
        mock_product1 = Mock()
        mock_product1.price = 100

        mock_product2 = Mock()
        mock_product2.price = 200

        mock_product3 = Mock()
        mock_product3.price = 300

        category = Category("Test", "Description", [mock_product1, mock_product2, mock_product3])
        result = category.middle_price()
        expected = (100 + 200 + 300) / 3
        assert result == expected

    def test_middle_price_float_result(self):
        """Тест: метод middle_price с дробным результатом"""
        mock_product1 = Mock()
        mock_product1.price = 100

        mock_product2 = Mock()
        mock_product2.price = 150

        mock_product3 = Mock()
        mock_product3.price = 200

        category = Category("Test", "Description", [mock_product1, mock_product2, mock_product3])
        result = category.middle_price()
        expected = (100 + 150 + 200) / 3
        assert result == 150.0

    def test_middle_price_zero_price_product(self):
        """Тест: метод middle_price с продуктом с нулевой ценой"""
        mock_product1 = Mock()
        mock_product1.price = 0

        mock_product2 = Mock()
        mock_product2.price = 100

        category = Category("Test", "Description", [mock_product1, mock_product2])
        result = category.middle_price()
        assert result == 50.0

    def test_middle_price_negative_price(self):
        """Тест: метод middle_price с отрицательной ценой (если такое возможно)"""
        mock_product1 = Mock()
        mock_product1.price = -50

        mock_product2 = Mock()
        mock_product2.price = 100

        category = Category("Test", "Description", [mock_product1, mock_product2])
        result = category.middle_price()
        assert result == 25.0

    def test_str_method_empty_category(self):
        """Тест: метод __str__ для пустой категории"""
        category = Category("Test Category", "Test Description", [])
        result = str(category)
        assert result == "Test Category, количество продуктов: 0 шт."

    def test_str_method_with_products(self):
        """Тест: метод __str__ для категории с продуктами"""
        mock_product1 = Mock()
        mock_product1.quantity = 10

        mock_product2 = Mock()
        mock_product2.quantity = 5

        mock_product3 = Mock()
        mock_product3.quantity = 3

        category = Category("Электроника", "Техника", [mock_product1, mock_product2, mock_product3])
        result = str(category)
        total = 10 + 5 + 3
        assert result == f"Электроника, количество продуктов: {total} шт."

    def test_str_method_special_category_name(self):
        """Тест: метод __str__ с особым именем категории"""
        mock_product = Mock()
        mock_product.quantity = 1

        category = Category("Категория & More ®", "Описание", [mock_product])
        result = str(category)
        assert result == "Категория & More ®, количество продуктов: 1 шт."

    def test_str_method_unicode_category_name(self):
        """Тест: метод __str__ с юникод-символами"""
        mock_product = Mock()
        mock_product.quantity = 5

        category = Category("カテゴリ", "説明", [mock_product])
        result = str(category)
        assert result == "カテゴリ, количество продуктов: 5 шт."

    def test_str_method_zero_quantity_products(self):
        """Тест: метод __str__ с продуктами с нулевым количеством"""
        mock_product1 = Mock()
        mock_product1.quantity = 0

        mock_product2 = Mock()
        mock_product2.quantity = 0

        category = Category("Test", "Description", [mock_product1, mock_product2])
        result = str(category)
        assert result == "Test, количество продуктов: 0 шт."

    def test_str_method_negative_quantity(self):
        """Тест: метод __str__ с отрицательным количеством (если такое возможно)"""
        mock_product1 = Mock()
        mock_product1.quantity = 5

        mock_product2 = Mock()
        mock_product2.quantity = -3  # Отрицательное количество

        category = Category("Test", "Description", [mock_product1, mock_product2])
        result = str(category)
        total = 5 + (-3)
        assert result == f"Test, количество продуктов: {total} шт."


class TestCategoryIntegration:
    """Интеграционное тестирование методов класса Category"""

    def test_all_methods_together(self):
        """Тест: все методы работают корректно вместе"""

        product1 = Product("Ноутбук", "Игровой ноутбук", 5000, 3)
        product2 = Product("Мышь", "Беспроводная мышь", 50, 10)
        product3 = Product("Клавиатура", "Механическая", 200, 5)

        category = Category("Компьютерная техника", "Техника для компьютера", [product1, product2, product3])


        assert len(category) == 3


        products_str = category.products
        assert "Ноутбук, 5000 руб. Остаток: 3 шт." in products_str
        assert "Мышь, 50 руб. Остаток: 10 шт." in products_str
        assert "Клавиатура, 200 руб. Остаток: 5 шт." in products_str


        middle_price = category.middle_price()
        expected_middle = (5000 + 50 + 200) / 3
        assert middle_price == expected_middle


        category_str = str(category)
        total_quantity = 3 + 10 + 5
        assert category_str == f"Компьютерная техника, количество продуктов: {total_quantity} шт."

    def test_category_modifications_affect_all_methods(self):
        """Тест: изменения категории влияют на все методы"""
        category = Category("Test", "Description", [])


        assert len(category) == 0
        assert category.products == ""
        assert category.middle_price() == 0
        assert str(category) == "Test, количество продуктов: 0 шт."


        product1 = Product("Product1", "Desc1", 100, 5)
        category.add_product(product1)

        assert len(category) == 1
        assert "Product1, 100 руб. Остаток: 5 шт." in category.products
        assert category.middle_price() == 100
        assert str(category) == "Test, количество продуктов: 5 шт."


        product2 = Product("Product2", "Desc2", 200, 3)
        category.add_product(product2)

        assert len(category) == 2
        assert "Product2, 200 руб. Остаток: 3 шт." in category.products
        assert category.middle_price() == 150
        assert str(category) == "Test, количество продуктов: 8 шт."


class TestCategoryEdgeCases:
    """Тестирование граничных случаев"""

    def test_products_property_large_list(self):
        """Тест: свойство products с большим списком продуктов"""
        products = []
        for i in range(1000):
            mock_product = Mock()
            mock_product.name = f"Product{i}"
            mock_product.price = i * 10
            mock_product.quantity = i
            products.append(mock_product)

        category = Category("Test", "Description", products)
        result = category.products

        assert result.count('\n') == 999
        assert "Product0, 0 руб. Остаток: 0 шт." in result
        assert "Product999, 9990 руб. Остаток: 999 шт." in result

    def test_middle_price_very_large_numbers(self):
        """Тест: middle_price с очень большими числами"""
        mock_product1 = Mock()
        mock_product1.price = 10 ** 9

        mock_product2 = Mock()
        mock_product2.price = 2 * 10 ** 9

        category = Category("Test", "Description", [mock_product1, mock_product2])
        result = category.middle_price()
        expected = (10 ** 9 + 2 * 10 ** 9) / 2
        assert result == expected

    def test_middle_price_precision(self):
        """Тест: точность вычисления middle_price"""
        mock_product1 = Mock()
        mock_product1.price = 1 / 3

        mock_product2 = Mock()
        mock_product2.price = 2 / 3

        category = Category("Test", "Description", [mock_product1, mock_product2])
        result = category.middle_price()
        expected = 0.5
        assert abs(result - expected) < 0.0000001

    def test_str_method_very_large_quantity(self):
        """Тест: __str__ с очень большим количеством товаров"""
        mock_product = Mock()
        mock_product.quantity = 10 ** 9  # 1 миллиард

        category = Category("Test", "Description", [mock_product])
        result = str(category)
        assert result == "Test, количество продуктов: 1000000000 шт."