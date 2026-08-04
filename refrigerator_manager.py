import json
from datetime import date
from model.refrigerator import Food


def main_menu():
    print("""
    --------------- REFRIGERATOR ---------------
    0. 프로그램 종료
    1. 냉장고에 음식 넣기
    2. 냉장고 음식 목록
    3. 냉장고 음식 조회
    4. 냉장고 음식 섭취
    5. 냉장고 음식 폐기
    6. 섭취 음식 목록
    7. 폐기 음식 목록
    8. 자동음식추가 (테스트/시연)
    """)


# 1. 냉장고에 음식 넣기 // name, price, calories, exp_date)
def food_in():
    food_list = select_list("food_data.json")
    print("--------------- 냉장고에 음식 넣기 ---------------")
    with open("food_data.json", "w", encoding="utf-8") as f:
        name = input("음식 이름 : ")
        price = int(input("음식 가격(원) : "))
        calories = int(input("음식 칼로리(Kcal) : "))
        input_date = input("음식 유통기한(XXXX-XX-XX): ")
        exp_date = date.fromisoformat(input_date)
        food = Food(name, price, calories, exp_date)
        food_dict = food.to_dict()
        food_list.append(food_dict)
        json.dump(food_list, f, ensure_ascii=False, indent=2)
    print("------------- 냉장고에 음식 넣기 완료 ------------")


def select_list(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


# 2. 냉장고 음식 목록
def refrigerator_food_list(food_list):
    print("--------------- 냉장고 음식 목록 ---------------")
    if len(food_list) < 1:
        print("냉장고가 비었습니다.")
        return
    print("번호 | 음식")
    for idx, food in enumerate(food_list):
        food = Food.from_dict(food)
        line = f"{idx}.  | {food.name}"
        if food.if_food_expired():
            line += "  (상한음식)"
        print(line)
    print("----------- 냉장고 음식 목록 조회 완료 -----------")


# 3. 음식 조회
def food_detail(food_list):
    print("--------------- 냉장고 음식 상세 조회 ---------------")
    number = int(input("음식 번호 : "))
    print("번호 | 음식")
    food = Food.from_dict(food_list[number])
    print(f"{number}.  | {food}")
    print("------------ 냉장고 음식 상세 조회 완료 -------------")


# 4. 음식 섭취
def eat_food(food_list):
    print("--------------- 냉장고 음식 섭취 ---------------")
    number = int(input("음식 번호 : "))
    food = Food.from_dict(food_list[number])
    result = food.if_food_expired()
    if result:
        print(f"음식 : {food.name} / 유통기한 : {food.exp_date}")
        print("유통기한이 지난 음식은 섭취 할수 없습니다.")
    else:
        consumed_food_list = select_list("consumed_data.json")
        with open("consumed_data.json", "w", encoding="utf-8") as f:
            consumed_food = food
            consumed_food_dict = consumed_food.to_dict()
            consumed_food_list.append(consumed_food_dict)
            json.dump(consumed_food_list, f, ensure_ascii=False, indent=2)
            print(f"{food.name} 섭취로 획득한 칼로리 :  {food.calories} Kcal")
            with open("food_data.json", "w", encoding="utf-8") as f:
                del food_list[number]
                json.dump(food_list, f, ensure_ascii=False, indent=2)
    print("------------- 냉장고 음식 섭취 완료 ------------")


# 5. 음식 폐기
def disposal_food(food_list):
    print("--------------- 상한 음식 폐기 ---------------")
    number = int(input("음식 번호 : "))
    food = Food.from_dict(food_list[number])
    result = food.if_food_expired()
    if result != True:
        print(f"음식 : {food.name} / 유통기한 : {food.exp_date}")
        print("유통기한이 남은 음식은 폐기 할수 없습니다.")
    else:
        wasted_food_list = select_list("wasted_data.json")
        with open("wasted_data.json", "w", encoding="utf-8") as f:
            wasted_food = food
            wasted_food_dict = wasted_food.to_dict()
            wasted_food_list.append(wasted_food_dict)
            json.dump(wasted_food_list, f, ensure_ascii=False, indent=2)
            print(f"{food.name} 폐기로 낭비된 금액 :  {food.price} 원")
            with open("food_data.json", "w", encoding="utf-8") as f:
                del food_list[number]
                json.dump(food_list, f, ensure_ascii=False, indent=2)
    print("------------- 상한 음식 폐기 완료 ------------")


# 6. 음식 섭취 리스트
def food_consumed_list(consumed_list):
    print("--------------- 섭취 음식 목록 ---------------")
    if len(consumed_list) < 1:
        print("섭취 음식이 없습니다.")
        return
    print("번호 |  음식 이름 / 칼로리(Kcal)")
    food_consumed_kcal = 0
    for idx, food in enumerate(consumed_list):
        consumed_food = Food.from_dict(food)
        print(f"{idx}.  |  {consumed_food.name} / {consumed_food.calories} Kcal")
        food_consumed_kcal += consumed_food.calories
    print(f"총 섭취 칼로리 :  {food_consumed_kcal} Kcal")
    print("----------- 섭취 음식 목록 조회 완료 -----------")


# 7. 음식 폐기 리스트
def food_wasted_list(wasted_list):
    print("--------------- 폐기 음식 목록 ---------------")
    if len(wasted_list) < 1:
        print("폐기 음식이 없습니다.")
        return
    print("번호 |  음식 이름 / 가격(원)")
    food_wasted_price = 0
    for idx, food in enumerate(wasted_list):
        wasted_food = Food.from_dict(food)
        print(f"{idx}.  |  {wasted_food.name} / {wasted_food.price} 원")
        food_wasted_price += wasted_food.price
    print(f"음식 폐기로 낭비된 총액 :  {food_wasted_price} 원")
    print("----------- 폐기 음식 목록 조회 완료 -----------")


def run_refrigerator_manager():
    number = input("번호 입력 : ")
    match number:
        case "1":
            food_in()
        case "2":
            food_list = select_list("food_data.json")
            refrigerator_food_list(food_list)
        case "3":
            food_list = select_list("food_data.json")
            food_detail(food_list)
        case "4":
            food_list = select_list("food_data.json")
            eat_food(food_list)
        case "5":
            food_list = select_list("food_data.json")
            disposal_food(food_list)
        case "6":
            consumed_list = select_list("consumed_data.json")
            food_consumed_list(consumed_list)
        case "7":
            wasted_list = select_list("wasted_data.json")
            food_wasted_list(wasted_list)
        case "8":
            auto_in()
        case "0":
            return True
        case _:
            print("잘못된 입력입니다.")


#### 테스트/시연용 자동 음식 넣기.
def auto_in():
    food_list = select_list("food_data.json")
    with open("food_data.json", "w", encoding="utf-8") as f:
        foods = [
            ("사과", 1500, 140, "2026-09-01"),
            ("망고", 4500, 340, "2026-07-21"),
            ("햄버거", 10000, 950, "2026-09-21"),
            ("감자샐러드", 7500, 650, "2026-09-15"),
            ("피자", 13000, 1200, "2026-07-01"),
            ("짬뽕", 11500, 1000, "2026-10-01"),
            ("배", 1700, 200, "2026-07-12"),
            ("대추", 1700, 275, "2026-06-12"),
            ("복숭아", 8900, 325, "2026-10-12"),
            ("콜라", 2000, 565, "2027-11-13")
        ]
        for name, price, calories, exp_date in foods:
            food = Food(name=name, price=price, calories=calories, exp_date=date.fromisoformat(exp_date))
            food_dict = food.to_dict()
            food_list.append(food_dict)
        json.dump(food_list, f, ensure_ascii=False, indent=2)

    print("--------- 냉장고에 자동 음식 넣기 완료 ---------")
