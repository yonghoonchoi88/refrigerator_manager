from datetime import date


class Food:
    def __init__(self, name, price, calories, exp_date):
        self.name = name
        self.price = price
        self.calories = calories
        self.exp_date = exp_date
        today = date.today()
        self.days_left = (self.exp_date - today).days


    def if_food_expired(self):
        if self.days_left > 0:
            return False
