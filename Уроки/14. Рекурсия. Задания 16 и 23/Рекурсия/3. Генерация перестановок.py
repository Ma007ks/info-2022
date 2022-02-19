def print_permutations(lst, permutation):
    if len(lst) == 0:
        print(permutation)
        return

    for i in range(len(lst)):
        element = lst.pop(i)
        if element not in permutation:
            permutation.append(element)
        print_permutations(lst, permutation)
        lst.insert(i, element)
        permutation.remove(element)


print_permutations([1, True, True, "Hello"], [])
