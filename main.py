from refrigerator_manager import run_refrigerator_manager, main_menu

print("--------------- REFRIGERATOR MANAGER PROGRAM ---------------")

while True:
    try:
        main_menu()
        run_refrigerator_manager()
    except Exception as e:
        print(e)