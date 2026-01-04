from src.product_category import Product


def test_products_category(product_category):
    product = product_category._Category__products[0]
    product1 = product_category._Category__products[1]
    product2 = product_category._Category__products[2]
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product1.name == "Iphone 15"
    assert product2.name == "Xiaomi Redmi Note 11"
    assert product_category.name == "Смартфоны"


def test_new_price(product_category):
    product = product_category._Category__products[0]
    product1 = product_category._Category__products[1]
    product2 = product_category._Category__products[2]
    assert product.price == 180000.0
    assert product1.price == 210000.0
    assert product2.price == 31000.0


def test_add_new_product(existing_products):
    new_info = {"name": "Xiaomi Redmi Note 11", "description": "1024GB, Синий", "price": 31000.0, "quantity": 14}
    new_product = Product.new_product(new_info, existing_products)
    assert new_product.name == "Xiaomi Redmi Note 11"
    assert len(existing_products) == 3


def test_update_existing_product(existing_products):
    existing_info = {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера",
                     "price": 170000.0, "quantity": 2}
    updated_product = Product.new_product(existing_info, existing_products)
    assert updated_product.quantity == 7  # Проверяем, что количество обновлено
    assert updated_product.price == 180000.0
