n = int(input("Введите номер четверти: ")) # создаём переменную n и присваем ей целочисленные значения, которые пользователь вводитс клавиатуры, после вывода сообщения, с предложением ввести номер четверти

if (n == 1): # если проверка переменной n на равенство 1 оказывается верной, то тогда
    print(f"Диапазон возможных координат точек в этой четверти в плоскости Х: от 1 до бесконечности, в плоскости Y: от 1 до бесконечности") # выводим сообщение на экран, о том, что диапазон возможных координат точек в этой четверти в плоскости Х: от 1 до бесконечности, в плоскости Y: от 1 до бесконечности
if (n == 2): #  если проверка переменной n на равенство 2 оказывается верной, то тогда
    print(f"Диапазон возможных координат точек в этой четверти в плоскости Х: от -1 до  минус бесконечности, в плоскости Y: от 1 до бесконечности") # выводим сообщение на экран, о том, что диапазон возможных координат точек в этой четверти в плоскости Х: от -1 до  минус бесконечности, в плоскости Y: от 1 до бесконечности
if (n == 3): # если проверка переменной n на равенство 3  оказывается верной, то тогда
    print(f"Диапазон возможных координат точек в этой четверти в плоскости Х: от -1 до минус бесконечности, в плоскости Y: от -1 до минус бесконечности") #  выводим сообщение на экран, о том, что диапазон возможных координат точек в этой четверти в плоскости Х: от -1 до минус бесконечности, в плоскости Y: от -1 до минус бесконечности
if (n == 4): # если проверка переменной n на равенство 4  оказывается верной, то тогда
    print(f"Диапазон возможных координат точек в этой четверти в плоскости Х: от 1 до бесконечности, в плоскости Y: от -1 до минус бесконечности") # выводим сообщение на экран, о том, что диапазон возможных координат точек в этой четверти в плоскости Х: от 1 до бесконечности, в плоскости Y: от -1 до минус бесконечности
if (n > 5) or (n < 1): # если переменная n оказывается > 5 или <1, то тогда
    print("Вы ввели неправильный номер четверти") # выводим сообение на экран, о том, что пользователь ввёл неправильный номер четверти
