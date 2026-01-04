class Product:
    name: str
    description: str
    price: float
    quantity: str

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, product_info, existing_products):
        new_product = cls(**product_info)

        for product in existing_products:
            if product.name == new_product.name:
                product.quantity += new_product.quantity
                product.price = max(product.price, new_product.price)
                return product

        existing_products.append(new_product)
        return new_product

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        elif new_price < self.__price:
            confirm = input("Цена товара понижается. Подтвердите изменение (y/n): ")
            if confirm.lower() == 'y':
                self.__price = new_price
        else:
            self.__price = new_price


class Category:
    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, __products: list[Product]):
        self.name = name
        self.description = description
        self.__products = __products
        self.__products = __products if __products else []
        Category.category_count += 1
        Category.product_count += len(__products) if __products else 0

    @property
    def products(self):
        return "\n".join(
            [f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт." for product in self.__products]
        )

    def add_product(self, product):
        self.__products.append(product)
