from typing import List, Tuple


def monotonic_subarray(arr: List[int]) -> Tuple[int, int]:
    """
    Находит наибольшую монотонную подпоследовательность
    (возрастающую или убывающую)
    в данном массиве и возвращает индексы первого
    и последнего элементов этой подпоследовательности
    :param arr: (list): список целых чисел
    :return: max_left (int): индекс первого элемента наибольшей монотонной подпоследовательности в arr
            max_right (int): индекс последнего элемента наибольшей монотонной подпоследовательности в arr
    """
    n = len(arr)
    left = right = 0
    max_length = 0
    if n == 1 or len(set(arr)) == 1:
        return 0, 0

    while right < n - 1:
        # ищем монотонный ряд
        while right < n - 1 and arr[right] == arr[right + 1]:
            right += 1

        if right < n - 1 and arr[right] < arr[right + 1]:
            # возрастающий ряд
            while right < n - 1 and arr[right] < arr[right + 1]:
                right += 1
        elif right < n - 1 and arr[right] > arr[right + 1]:
            # убывающий ряд
            while right < n - 1 and arr[right] > arr[right + 1]:
                right += 1

        # обновляем максимальную длину
        if right - left + 1 > max_length:
            max_length = right - left + 1
            max_left = left
            max_right = right
        # сдвигаем левый указатель
        left = right

    return max_left, max_right





if __name__ == '__main__':
    arr = [-3, 2, 3, 4, 5, 6, 7, 7, 8]
    print(monotonic_subarray(arr))

    arr = [-1, -1, -1, -1, -1, -1, -1, -1, -1]
    print(monotonic_subarray(arr))