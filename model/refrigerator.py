from datetime import date


class Food:
    def __init__(self, name, price, calories, exp_date):
        self.name = name
        self.price = price
        self.calories = calories
        self.exp_date = exp_date
        today = date.today()
        self.days_left = (self.exp_date - today).days

    def __str__(self):
        return f"{self.name}, {self.price}원, {self.calories}칼로리(Kcal), 유통기한 {self.exp_date}"

    def to_dict(self) -> dict:
        return {"name": self.name, "price": self.price, "calories": self.calories, "exp_date": self.exp_date.isoformat()}

    @staticmethod
    def from_dict(food_data) -> Food:
        exp_date = date.fromisoformat(food_data["exp_date"])
        return Food(name = food_data["name"], price = food_data["price"], calories = food_data["calories"], exp_date = exp_date)

    def if_food_expired(self):
        if self.days_left < 0:
            return True
        else:
            return False
