coordinate_x = int(input('Введите координату по оси Х: '))
coordinate_y = int(input('Введите координату по оси Y: '))

if coordinate_x == 0 and coordinate_y > 0:
    print('Точка находится на оси Х между четвертями 1 и 2')
elif coordinate_x == 0 and coordinate_y < 0:
    print('Точка находится на оси X между четвертями 3 и 4')
elif coordinate_y == 0 and coordinate_x > 0:
    print('Точка находится на оси Y между четвертями 1 и 4')
elif coordinate_y == 0 and coordinate_x < 0:
    print('Точка находится на оси Y между четвертями 2 и 3')
elif coordinate_x > 0 and coordinate_y > 0:
    print(1)
elif coordinate_x < 0 and coordinate_y > 0:
    print(2)
elif coordinate_x < 0 and coordinate_y < 0:
    print(3)
else:
    print(4)