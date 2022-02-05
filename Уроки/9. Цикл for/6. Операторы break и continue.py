# break прерывает цикл (досрочно завершаем его) — прекратить
# continue прерывает итерацию (досрочно завершаем текущую итерацию) — продолжить

# for i in range(10):
#     print(i)
#     if i > 4:
#         break

numbers = [235, 124, 634, 2, 5, 231]

# print(124 in numbers)
# print(-124 in numbers)

result = False
for x in numbers:
    if x == 124:
        result = True
        break

print(result)
