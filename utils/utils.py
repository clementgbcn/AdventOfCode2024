import bisect
import re
from typing import List, Callable

INT_PATTERN = re.compile(r"-?\d+")


def extract_int(sentence: str) -> List[int]:
    return list(map(int, INT_PATTERN.findall(sentence)))


def insert_sorted(
    seq: List[any],
    keys: List[any],
    item: any,
    key_func: Callable[[any], any] = lambda v: v,
) -> None:
    k = key_func(item)
    i = bisect.bisect_left(keys, k)
    keys.insert(i, k)
    seq.insert(i, item)
