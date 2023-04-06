ticket = int(input('Введите необходимое колличество билетов: '))
age = int(input('Введите возраст: '))

if age < 18:
    ticket_price = 0
    print("Конференция бесплатная!")
elif 18 <= age < 25:        # по условию не совсем поняла интервалы, если с 25 лет - это уже третий интервал, посчитала, что 25 во второй интервал не входит
    ticket_price = 999
    full_cost = ticket_price * ticket
    print("Стоимость заказа билетов: ", full_cost, 'руб.')
else:
    ticket_price = 1390
    full_cost = ticket_price * ticket
    print("Стоимость заказа билетов: ", full_cost, 'руб.')

if ticket >= 3 and age >= 18:
    discount = round((ticket_price * ticket) * 10 / 100) # округлила, чтобы скидка лучше выглядила
    print('---')
    print('10% скидка составила: ', discount, "руб.")
    full_cost_2 = (ticket_price * ticket) - discount
    print('Общая стоимость заказа: ', full_cost_2, "руб.")