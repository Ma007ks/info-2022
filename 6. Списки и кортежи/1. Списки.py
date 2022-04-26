# Список (list) — это упорядоченный изменяемый набор объектов.

lst = [7, 3, 4, -1, 5]
#      0  1  2   3  4
#     -5 -4 -3  -2 -1

print("Сам список:", lst)
print("Сколько в нём элементов?", len(lst))

print("\nИндексация:")
print(f"{lst[0] = }")
print(f"{lst[1] = }")
print(f"{lst[4] = }")
print(f"{lst[-1] = } — последний элемент")
print(f"{lst[len(lst) - 1] = } — последний элемент")
print(f"{lst[-3] = }")

# x[start:finish:step]
# — берём элементы с start до finish не включительно с шагом step
# — получаем новый список
print("\nСрезы:")
print("lst[0:3] = lst[:3] =", lst[:3], "— первые 3 элемента")
print("lst[3:] =", lst[3:], "— все, кроме первых 3")
print("lst[1:3] =", lst[1:3])
print("lst[:-2] =", lst[:-2], "— все, кроме двух последних")
print("lst[::2] =", lst[::2])
print("lst[::-1] =", lst[::-1], "— разворот списка")
print("lst[::] =", lst[::], "— копия списка")

print("\nИзменение элемента списка:")
lst[1] = 10  # изменение некоторого элемента
print(lst)

print("\nДобавление новых элементов в список:")
lst.append(250)  # вставка элемента в конец списка
print(lst)

lst.extend([7, 2])  # добавить в список элементы другого списка или iterable
print(lst)

lst.insert(2, False)
print(lst)
lst.insert(0, 777)  # вставка элемента в начало списка
print(lst)

print("\nУдаление элементов из списка:")
lst.remove(False)  # удаление первого вхождения объекта
print(lst)

print(lst.pop())  # выталкиваем (удаляем) элемент с определённой позиции
print(lst)
print(lst.pop())
print(lst)
print(lst.pop(0))
print(lst)

del lst[0]  # lst.pop(0), del от delete, удалить
print(lst)

print("\nИзменение списка полностью:")
# lst.clear()  # очистить список

lst.insert(3, 9)
lst.insert(0, 15)
print(lst, "— до сортировки")

lst.sort()
print(lst, "— в возрастающем порядке (неубывающем)")
lst.sort(reverse=True)
print(lst, "— в убывающем порядке (невозрастающем)")


def sum_digits(x):
    return sum(map(int, str(abs(x))))


lst.sort(key=sum_digits)
print(lst, "— сортировка по сумме цифр")

lst.sort(key=lambda x: abs(x) % 10)
print(lst, "— сортировка по младшей цифры")

lst.reverse()
print(lst, "— развернули список")

print("\nЕщё две функции:")

lst.extend([3, 3.0, 4, 5, 3.0, 2, 3])
print(lst)

print(lst.count(3), "— количество троек в списке")

print(lst.index(3), "— первый индекс тройки")
print(lst.index(3, 9))
