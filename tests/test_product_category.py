def test_products_category(product_category):
    assert product_category.products[0].name == "Samsung Galaxy S23 Ultra"
    assert product_category.products[1].name == "Iphone 15"
    assert product_category.products[2].name == "Xiaomi Redmi Note 11"
    assert product_category.name == "Смартфоны"
