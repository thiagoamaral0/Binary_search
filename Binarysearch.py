def binary_search(array, item, begin = 0, end = None):
    if end is None:
        end = len(array) - 1
    if begin <= end:
        middle = (begin + end) // 2
        if array[middle] == item:
            return middle
        if item < array[middle]:
            return binary_search(array, item,begin, middle - 1)
        if item > array[middle]:
            return binary_search(array, item, middle + 1, end)
    return None


Numbers = [3, 8, 11, 14, 16, 19, 25, 29, 31, 37, 42, 46, 53, 58, 60, 63, 71, 82]
choose = int(input("Search for a number: "))
while choose != 0:
    result = binary_search(Numbers, choose)
    if result in Numbers:
        print("The number {} exists.Its position is {}".format(choose, result))
        break
    else:
        print("This number not exists in list.")
        break