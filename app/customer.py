class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list,
            money: int,
            car: dict
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def money_info(self) -> None:
        print(f"{self.name} has {self.money} dollars")

    def less_money_info(self) -> None:
        print(f"{self.name} doesn't have enough money to make purchase "
              f"in any shop")