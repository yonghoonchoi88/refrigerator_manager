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

    def if_food_expired(self):
        if self.days_left < 0:
            return True
        else:
            return False
