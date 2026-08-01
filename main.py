from refrigerator_manager import run_refrigerator_manager, main_menu

print("--------------- REFRIGERATOR MANAGER PROGRAM ---------------")

while True:
    try:
        main_menu()
        result = run_refrigerator_manager()
        if result:
            print("--------------- REFRIGERATOR MANAGER PROGRAM ENDED ---------------")
            break
    except Exception as e:
        print(e)
