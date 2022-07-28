try:
        a = input('Введите первое число: ')
        b = input('Введите второе число :')
        result = int(a)/int(b)
except ZeroDivisionError:
        print("Всё плохо, давай по новому")
else:
        print("Результат в квадрате :" , result **2)
finally:
        print("Пипец всему")

