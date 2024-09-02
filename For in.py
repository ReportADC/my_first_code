numbers = ['Раз', 'Два', 'Три', 'Четыре', 'Пять']
for number in numbers:
    print(number)
print('Вышел зайчик погулять')


sweets = ['Батончик', 'Сникерс', 'Мишка Косолапый', 'Коровка']
kids = ['Витя', 'Маша', 'Марина']
for kid in kids:
    for sweet in sweets:  
        print(kid, 'получает конфету', sweet)  



kids = ['Витя', 'Маша', 'Марина']
for kid in kids:
    print ('У Литейного моста')
    print('Я поймал в Неве кита,')
    print('Спрятал за окошко.')
    print('Съела его кошка,')
    print('Помогали два кота…')
    print('Вот и нет теперь кита!')
    print('Ты не веришь другу?')
    print('Выходи из круга!')
    print('* Из круга выходит', kid, '*')
    print()
print('Всё!')

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for number_1 in numbers:
    for number_2 in numbers:
        print(number_1, '*', number_2, '=', number_1 * number_2)