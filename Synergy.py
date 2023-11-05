print('Введите два числа А и В (по условию А < или = В)')
a = int(input('A: '))
b = int(input('B: '))
string = ''
if a <= b:
    for i in range(a, b + 1):
        if i % 2 == 0:
            string += '{i} '.format(i = i)
else:
    print('Неверно введены числа')
print(string)