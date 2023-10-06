str = input()
x = str.count('(')
y = str.count(')')
if x < y:
    print('не хватает', (y - x), 'открывающих скобок (')
elif x > y:
    print('не хватает', (x - y), 'закрывающих скобок )')
else:
    print('количество скобок одинаково')