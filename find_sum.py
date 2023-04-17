from itertools import chain, combinations
from typing import List, Tuple, Union


def powerset(iterable: List[Union[int, str]]) -> chain:
    """
    Возвращает все подмножества iterable.
    """
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))


def find_sum(n: int, m: int) -> str:
    """
    Расставляет знаки + между некоторыми цифрами числа N,
    чтобы в сумме получилось число M.
    Возвращает строку с правильной расстановкой знаков и значением M,
    или строку "Нет решений", если решение не найдено.
    """
    digits = list(range(1, n + 1))
    num_str = "".join(map(str, digits))
    for comb in powerset(range(1, len(num_str))):
        start = 0
        expr = ""
        for i in comb:
            expr += num_str[start:i] + "+"
            start = i
        expr += num_str[start:]
        if eval(expr) == m:
            return f"{expr}={m}"
    return "Нет решений"


if __name__ == "__main__":
    print(find_sum(5, 15))  # 1+2+3+4+5=15
    print(find_sum(4, 46))  # 12+34=46
