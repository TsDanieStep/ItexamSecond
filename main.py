menu = {
    1: {'name': 'Маргарита', 'price': 70000},
    2: {'name': 'Пепперони', 'price': 95000},
    3: {'name': 'Гавайская', 'price': 78000},
    4: {'name': 'Четыре сыра', 'price': 90000},
    5: {'name': 'Вегетарианская', 'price': 68000}
}

order = []

def display_menu():
    print('Меню:')
    for key, value in menu.items():
        print(f"{key}. {value['name']} - {value['price']} сум.")

def create_order():
    while True:
        display_menu()
        choice = input('Введите номер пиццы или "q" для выхода: ')
        if choice == 'q':
            break
        try:
            pizza_number = int(choice)
            if pizza_number in menu:
                order.append(menu[pizza_number])
                print(f"{menu[pizza_number]['name']} добавлена в заказ.")
            else:
                print("Неверный номер пиццы.")
        except ValueError:
            print("Неверный ввод.")

def confirm_order():
    print("Ваш заказ:")
    total_price = 0
    for pizza in order:
        print(f"{pizza['name']} - {pizza['price']} сум.")
        total_price += pizza['price']
    print(f"Итого: {total_price} сум.")
    while True:
        choice = input("Подтвердите заказ (y/n): ")
        if choice == 'y':
            print("Заказ подтвержден.")
            return True
        elif choice == 'n':
            print("Заказ отменен.")
            return False
        else:
            print("Неверный ввод.")

def accept_payment(total_price):
    while True:
        payment = input(f"Введите сумму оплаты ({total_price} сум.): ")
        try:
            payment_amount = int(payment)
            if payment_amount >= total_price:
                change = payment_amount - total_price
                print(f"Спасибо за оплату! Ваша сдача {change} сум.")
                return True
            else:
                print("Недостаточно средств.")
        except ValueError:
            print("Неверный ввод.")

def main():
    create_order()
    if confirm_order():
        total_price = sum([pizza['price'] for pizza in order])
        accept_payment(total_price)
        print("Заказ передан на выполнение.")
    else:
        print("Заказ не подтвержден.")

if __name__ == '__main__':
    main()


