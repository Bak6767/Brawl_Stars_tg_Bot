from database.bd import clear_all_cells
import asyncio
import os

def admin_cmd():
    while True:
        a = input("bak6767 :")
        if a == "reset_db":
            # Создаем новый событийный цикл
            loop = asyncio.new_event_loop()
            # Запускаем асинхронную функцию в событийном цикле
            loop.run_until_complete(clear_all_cells())
            loop.close()
            print("База данных успешно очищена")
        elif a == "cls":
            os.system('cls' if os.name == 'nt' else 'clear')
        elif a == "real_cmd":
            os.system('start cmd')
        elif a == "help":
            print("\nreset_db - очищает базу данных\ncls - очистка командной строки vscode\nreal_cmd - открывает cmd\n")
        else:
            print("Неизвестная команда")


