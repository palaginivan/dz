x = input()
s = []
while x:
    s.append(x)
    x = input()
s.sort(reverse = True)
print(''.join(s))

