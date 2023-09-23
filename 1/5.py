x = float(input())
y = float(input())
if x > 0 and y > 0:
    print('точка в первой четверти')
elif x < 0 and y > 0:
    print('точка во второй четверти')
elif x < 0 and y < 0:
    print('точка в третьей четверти')
elif x > 0 and y < 0:
    print('точка в четвертой четверти')
elif x == 0 and y != 0:
    print('точка лежит на оси ординат')
elif y == 0 and x != 0:
    print('точка лежит на оси абсцисс')
else: 
    print('точка лежит в начале координат')