d = int(input('Введите длину стен: '))
e = int(input('Введите ширину стен: '))
p1 = (d + e) * 2
print(p1)
print('Введите высоту стены')
p2 = int(p1 * int(input('')))
print(p2)

print('Площадь деврных и оконных проемов')
o1 = (int(input()) * int(input()))
d1 = (int(input()) * int(input()))
pp = o1 + d1
print(pp)

print(p2 - pp)

a = int(input('Введите длину: '))
b = int(input('Введите ширину: '))
c = int(input('Введите высоту: '))

pb1 = (a * c)
print(pb1)
print('Введите полученую площать коробки')
pk = int(input())
print((pk / pb1) * 100)
print()