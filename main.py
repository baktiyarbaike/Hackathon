
from views import *
def main():
    while True:
        print('1 - Создание записей\n2 - Получения списка записей\n3 - Получения одной записи\n4 - Обновления записей\n5 - Удаления записей')

        choice = input('Выберите действие (1, 2, 3, 4, 5:) - ')
        if choice == '1':
            print(create_product())
        elif choice == '2':
            print(get_data())
        elif choice == '3':
            print(get_one_product())
        elif choice == '4':
            print(update_product())
        elif choice == '5':
            print(delete_product())
        else:
            print('Такого действия нет!')

        choice = input('Вы хотите продолжить? Да/Нет: ').lower()
        if choice == 'да':
            main()
        else:
            print('До свидания:)') 
            break

main()