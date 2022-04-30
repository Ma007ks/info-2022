def get_info(numbers):
    sm = 0  # сумма обработанных чисел
    ln = 0  # количество обработанных чисел
    rems_info = {}
    for x in numbers:
        sm += x
        ln += 1
        if sm % k not in rems_info:
            rems_info[sm % k] = (sm, ln)
    return rems_info


numbers = [int(v) for v in open("27-b.txt").read().splitlines()][1:]

k = 43
full_sum = sum(numbers)
left = get_info(numbers)
right = get_info(numbers[::-1])
max_sum = min_len = 0
for x in left:
    for y in right:
        if (full_sum - x - y) % k == 0 and left[x][1] + right[y][1] <= len(numbers):
            curr_sum = full_sum - left[x][0] - right[y][0]
            curr_len = len(numbers) - left[x][1] - right[y][1]
            if curr_sum > max_sum:
                max_sum = curr_sum
                min_len = curr_len
            elif curr_sum == max_sum and curr_len < min_len:
                min_len = curr_len
print(min_len)

"""
    0	731	1                               7	2217861876	3340775
    12	12646011	24526                   38	2844860301	4555642
    18	117082697	227286                  32	2536831945	3958607
    37	425110249	824321
    41	744081071	1442153
    29	851227599	1649870
    39	1044820790	2025132
    35	1168427640	2264910
    42	1178002371	2283570
    1	1373768086	2663049
    5	1428146535	2768408
    6	1473781576	2857143
    7	2217861833	3701302
    
    
    
    0	43	1
    1	744080257	1081626
    2	1488160514	1925785
    9	1533796507	2014520
    6	1552444572	2050661
    8	1588174650	2119879
    11	1635504495	2211479
    15	1783939854	2499358
    21	1917121997	2757796

    13	2505893598	3898849
    
    
"""
