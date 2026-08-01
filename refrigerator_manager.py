from unittest import case

from model.refrigerator import Food

refrigerator = []

def main_menu():
    print("""
    --------------- REFRIGERATOR ---------------
    0. 프로그램 종료
    1. 냉장고에 음식 넣기
    2. 냉장고 음식 목록
    3. 냉장고 음식 조회
    4. 냉장고 상한 음식 조회
    5. 냉장고 음식 섭취
    6. 냉장고 음식 폐기
    """)


# 냉장고에 음식 넣기 // name, price, calories, exp_date)
def food_in():
    name = input("음식 이름 : ")
    price = input("음식 가격 : ")
    calories = input("음식 칼로리 : ")
    exp_date = input("음식 유통기한 : ")
    food = Food(name, price, calories, exp_date)
    refrigerator.append(food)


# 냉장고 음식 목록
def refrigerator_food_list():
    if len(refrigerator) < 1 :
        print("냉장고가 비었습니다.")
        return
    print("음식 번호  |  ")
    for idx, food in enumerate(refrigerator):
        print(f"{idx}. {food}")

# 음식 조회
# 상한 음식 조회
# 음식 섭취
# 음식 폐기

def run_refrigerator_manager():
    number = input("번호 입력 : ")
    match number:
        case "1": food_in()
        case "2": refrigerator_food_list()
        case "3": pass