from datetime import date
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


# 1. 냉장고에 음식 넣기 // name, price, calories, exp_date)
def food_in():
    print("--------------- 냉장고에 음식 넣기 ---------------")
    name = input("음식 이름 : ")
    price = int(input("음식 가격(원) : "))
    calories = int(input("음식 칼로리(Kcal) : "))
    input_date = input("음식 유통기한(XXXX-XX-XX): ")
    exp_date = date.fromisoformat(input_date)
    food = Food(name, price, calories, exp_date)
    refrigerator.append(food)
    print("------------- 냉장고에 음식 넣기 완료 ------------")


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
    print("----------- 냉장고 음식 목록 조회 완료 -----------")


# 3. 음식 조회
def food_detail():
    print("--------------- 냉장고 음식 상세 조회 ---------------")
    number = int(input("음식 번호 : "))
    print("번호 | 음식")
    print(f"{number}.  | {refrigerator[number]}")
    print("------------ 냉장고 음식 상세 조회 완료 -------------")


# 4. 음식 섭취
def eat_food():
    global food_consumed_kcal
    print("--------------- 냉장고 음식 섭취 ---------------")
    number = int(input("음식 번호 : "))
    result = refrigerator[number].if_food_expired()
    if result:
        print(f"음식 : {refrigerator[number].name} / 유통기한 : {refrigerator[number].exp_date}")
        print("유통기한이 지난 음식은 섭취 할수 없습니다.")
    else:
        food_consumed_kcal += refrigerator[number].calories
        consumed_list.append(refrigerator[number])
        print(f"{refrigerator[number].name} 섭취로 획득한 칼로리 :  {refrigerator[number].calories} Kcal")
        del refrigerator[number]
    print("------------- 냉장고 음식 섭취 완료 ------------")


# 5. 음식 폐기
def disposal_food():
    global wasted_money
    print("--------------- 상한 음식 폐기 ---------------")
    number = int(input("음식 번호 : "))
    result = refrigerator[number].if_food_expired()
    if result != True:
        print(f"음식 : {refrigerator[number].name} / 유통기한 : {refrigerator[number].exp_date}")
        print("유통기한이 남은 음식은 폐기 할수 없습니다.")
    else:
        wasted_money += refrigerator[number].price
        garbage.append(refrigerator[number])
        print(f"{refrigerator[number].name} 폐기로 낭비된 금액 :  {refrigerator[number].price} 원")
        del refrigerator[number]
    print("------------- 상한 음식 폐기 완료 ------------")


# 6. 음식 섭취 리스트
def food_consumed_list():
    print("--------------- 섭취 음식 목록 ---------------")
    if len(consumed_list) < 1:
        print("섭취 음식이 없습니다.")
        return
    print("번호 |  음식 이름 / 칼로리(Kcal)")
    for idx, food in enumerate(consumed_list):
        print(f"{idx}.  |  {food.name} / {food.calories} Kcal")
    print(f"총 섭취 칼로리 :  {food_consumed_kcal} Kcal")
    print("----------- 섭취 음식 목록 조회 완료 -----------")


# 7. 음식 폐기 리스트
def food_wasted_list():
    print("--------------- 폐기 음식 목록 ---------------")
    if len(garbage) < 1:
        print("폐기 음식이 없습니다.")
        return
    print("번호 |  음식 이름 / 가격(원)")
    for idx, food in enumerate(garbage):
        print(f"{idx}.  |  {food.name} / {food.price} 원")
    print(f"음식 폐기로 낭비된 총액 :  {wasted_money} 원")
    print("----------- 폐기 음식 목록 조회 완료 -----------")


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
            print("잘못된 입력입니다.")


#### 테스트/시연용 자동 음식 넣기.
def auto_in():
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
        refrigerator.append(Food(name=name, price=price, calories=calories, exp_date=date.fromisoformat(exp_date)))

    print("--------- 냉장고에 자동 음식 넣기 완료 ---------")
