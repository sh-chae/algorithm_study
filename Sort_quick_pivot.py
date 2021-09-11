# Hoare partition :대표적인 분할방식인 호어 분할을 기준으로 퀵정렬을 설명
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:]

    left = [x for x in tail if x <= pivot]
    right = [x for x in tail if x > pivot]

    return quick_sort(left)+[pivot]+quick_sort(right)


print(quick_sort(array))
