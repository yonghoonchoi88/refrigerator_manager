from datetime import date
from unittest import case

from model.refrigerator import Food

refrigerator = []
consumed_list = []
garbage = []
food_consumed_kcal = 0
wasted_money = 0


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


#### 테스트/시연용 자동 음식 넣기.
def auto_in():
    f1date = date.strptime("2026-09-01", "%Y-%m-%d")
    f1 = Food(name="사과", price=1500, calories=140, exp_date=f1date)
    refrigerator.append(f1)
    f2date = date.strptime("2026-07-01", "%Y-%m-%d")
    f2 = Food(name="망고", price=4500, calories=340, exp_date=f2date)
    refrigerator.append(f2)
    f3date = date.strptime("2026-09-01", "%Y-%m-%d")
    f3 = Food(name="햄버거", price=10000, calories=950, exp_date=f3date)
    refrigerator.append(f3)
    f4date = date.strptime("2026-09-01", "%Y-%m-%d")
    f4 = Food(name="감자샐러드", price=7500, calories=650, exp_date=f4date)
    refrigerator.append(f4)
    f5date = date.strptime("2026-06-01", "%Y-%m-%d")
    f5 = Food(name="피자", price=13000, calories=1200, exp_date=f5date)
    refrigerator.append(f5)


# 1. 냉장고에 음식 넣기 // name, price, calories, exp_date)
def food_in():
    print("--------------- 냉장고에 음식 넣기 ---------------")
    name = input("음식 이름 : ")
    price = int(input("음식 가격(원) : "))
    calories = int(input("음식 칼로리(Kcal) : "))
    input_date = input("음식 유통기한(XXXX-XX-XX): ")
    exp_date = date.strptime(input_date, "%Y-%m-%d")
    food = Food(name, price, calories, exp_date)
    refrigerator.append(food)
    print("-------------- 냉장고에 음식 넣기 완료 -------------")


# 2. 냉장고 음식 목록
def refrigerator_food_list():
    print("--------------- 냉장고 음식 목록 ---------------")
    if len(refrigerator) < 1:
        print("냉장고가 비었습니다.")
        return
    print("번호 | 음식")
    for idx, food in enumerate(refrigerator):
        line = f"{idx}.  | {food.name}"
        if refrigerator[idx].if_food_expired():
            line += "  (상한음식)"
        print(line)
    print("------------ 냉장고 음식 목록 조회 완료 ------------")


# 3. 음식 조회
def food_detail():
    print("--------------- 냉장고 음식 상세 조회 ---------------")
    number = int(input("음식 번호 : "))
    print("번호 | 음식")
    print(f"{number}.  | {refrigerator[number]}")
    print("------------- 냉장고 음식 상세 조회 완료 --------------")


# 4. 음식 섭취
def eat_food():
    global food_consumed_kcal
    print("--------------- 냉장고 음식 섭취 ---------------")
    number = int(input("음식 번호 : "))
    result = refrigerator[number].if_food_expired()
    if result:
        print("상한 음식은 섭취 할수 없습니다.")
    else:
        food_consumed_kcal += refrigerator[number].calories
        consumed_list.append(refrigerator[number])
        print(f"{refrigerator[number].name} 섭취로 획득한 칼로리 :  {refrigerator[number].wasted_money} Kcal")
        del refrigerator[number]
    print(f"총 섭취 칼로리 :  {food_consumed_kcal} Kcal")
    print("-------------- 냉장고 음식 섭취 완료 -------------")


# 5. 음식 폐기
def disposal_food():
    global wasted_money
    print("--------------- 상한 음식 폐기 ---------------")
    number = int(input("음식 번호 : "))
    result = refrigerator[number].if_food_expired()
    if result != True:
        print("유통 기한이 남은 음식은 폐기 할수 없습니다.")
    else:
        wasted_money += refrigerator[number].price
        garbage.append(refrigerator[number])
        print(f"{refrigerator[number].name} 폐기로 낭비된 금액 :  {refrigerator[number].wasted_money} 원")
        del refrigerator[number]
    print("-------------- 상한 음식 폐기 완료 -------------")


# 6. 음식 섭취 리스트
def food_consumed_list():
    print("--------------- 섭취 음식 목록 ---------------")
    if len(consumed_list) < 1:
        print("섭취 음식이 없습니다.")
        return
    print("번호 |  음식 이름 / 칼로리(Kcal)")
    for idx, food in enumerate(consumed_list):
        print(f"{idx}.  |  {food.name} / {food.calories}")
    print(f"총 섭취 칼로리 :  {food_consumed_kcal} Kcal")
    print("------------ 섭취 음식 목록 조회 완료 ------------")


# 7. 음식 폐기 리스트
def food_wasted_list():
    print("--------------- 폐기 음식 목록 ---------------")
    if len(garbage) < 1:
        print("폐기 음식이 없습니다.")
        return
    print("번호 |  음식 이름 / 가격(원)")
    for idx, food in enumerate(garbage):
        print(f"{idx}.  |  {food.name} / {food.price}")
    print("음식 폐기로 낭비된 총액 : ", wasted_money)
    print("------------ 폐기 음식 목록 조회 완료 ------------")


def run_refrigerator_manager():
    number = input("번호 입력 : ")
    match number:
        case "1":
            food_in()
        case "2":
            refrigerator_food_list()
        case "3":
            food_detail()
        case "4":
            eat_food()
        case "5":
            disposal_food()
        case "6":
            food_consumed_list()
        case "7":
            food_wasted_list()
        case "8":
            auto_in()
        case "0":
            return True
        case _:
            ("잘못된 입력입니다.")
