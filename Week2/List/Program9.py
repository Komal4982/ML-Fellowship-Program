def common_list(list1, list2):
    result = False
    for x in list1:
        for y in list2:
            if x == y:
                result = True
                return result
    return result


a = [1, 2, 3, 4, 5]
b = [5, 6, 7, 8, 9]
print(common_list(a, b))

a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9]
print(common_list(a, b))



