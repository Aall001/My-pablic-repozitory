def input_int(x):
    while True:
        s = input(x)
        try:
            return int(s)
        except ValueError:
            print('Вы ввели не число! Попробуйте ещё раз')

sequence_num = list(map(int, input('Введите последовательность чисел через пробел: ').split()))

numb = input_int('Введите число для поиска: ')

def qsort(s):
    if len(s) <= 1:
        return s

    elem = s[0]
    left = list(filter(lambda x: x < elem, s))
    center = [i for i in s if i == elem]
    right = list(filter(lambda x: x > elem, s))

    return qsort(left) + center + qsort(right)

sort = qsort(sequence_num)
print("Последовательный список чисел: ", sort)

#1 2 3 7 6 5 4 8 9 10

def binary_search(lst, search_item):
    left_ = 0
    right_ = len(lst) - 1
    searh_result = False

    while left_ < right_ and not searh_result:
        middle = (left_ + right_) // 2
        guess = lst[middle]
        if guess == search_item:
            searh_result = True
            return searh_result
        if guess > search_item:
            right_ = middle - 1
        else:
            left_ = middle + 1

lst = sort
search_item = numb
result = binary_search(lst, search_item)
if result:
    print(f'Число {search_item}: в списке найдено')
else:
    print(f'Число {search_item}: в списке не найдено!')

