from database.bd import clear_all_cells
import os

def admin_cmd():
    while True:
        a = input("bak6767 :")
        if a == "reset_db":
            clear_all_cells()
            print("База данных успешно очищена")
        elif a == "cls":
            os.system('cls' if os.name == 'nt' else 'clear')
        elif a == "real_cmd":
            os.system('start cmd')
        else:
            print("Неизвестная команда")

