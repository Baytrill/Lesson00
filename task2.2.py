print('Давай сравним числа и помотрим сколько чисел равны между собой.')
first=input('Напиши первое число: ')
second=input('Напиши второе число: ')
third =input('Напиши третье число: ')
if first == second and first == third:
    print('Равны между собой 3 числа')
elif first==second or first==third or second == third:
    print('Равны между собой 2 числа')
else:
    print('Равны между собой 0 чисел')