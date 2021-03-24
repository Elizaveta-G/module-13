try:
    tickets = int (input ("Сколько билетов Вы хотите приобрести? "))
except ValueError:
    print("Пожалуйста, корректное число билетов.")
Fcost = 0
for price in range(1,tickets+1):
    try:
        age = int(input("Введите возраст посетителя: "))
    except ValueError:
        print("Пожалуйста, введите корректный возраст посетителя. ")
        if age < 18:
            price = 0
        elif 18 <= age < 25:
            price = 990
        elif 25 <= age <= 130:
            price = 1390
        else:
            print("Пожалуйста, введите корректный возраст посетителя. ")
            if tickets > 3:
                Fcost = 0.9 * (Fcost + price)
            else:
                Fcost = Fcost + price
                print ("Общая стоимость: ", Fcost)

