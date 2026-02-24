from collections import Counter
from typing import TypeVar, Iterable, Optional, List, Any

T = TypeVar("T")


def most_common(items: Iterable[T]) -> Optional[T]:
    """Return the most frequent element from `items`, or ``None`` if empty.

    Uses ``collections.Counter`` for correctness and efficiency.
    """
    items_list = list(items)
    if not items_list:
        return None
    counter = Counter(items_list)
    return counter.most_common(1)[0][0]


def filter_not_in_case_insensitive(source: Iterable[Any], exclude: Iterable[Any]) -> List[Any]:
    """Return items from `source` whose string form (case-insensitive) is not in `exclude`.

    Comparison is done using ``str(item).casefold()`` to support consistent
    case-insensitive comparisons for non-ASCII text. Original items and order
    are preserved.
    """
    exclude_set = {str(x).casefold() for x in exclude}
    return [item for item in source if str(item).casefold() not in exclude_set]


def future_value(start: float, rate: float, years: int) -> float:
    """Compute future value after `years` compounding annually at `rate`.

    - `rate` is a decimal (e.g., 0.05 for 5%).
    - Raises ``ValueError`` for negative ``years`` and ``TypeError`` for non-numeric inputs.
    """
    if years < 0:
        raise ValueError("years must be non-negative")
    try:
        s = float(start)
        r = float(rate)
    except Exception as exc:
        raise TypeError("start and rate must be numbers") from exc
    return s * (1 + r) ** years


if __name__ == "__main__":
    print(most_common([1, 2, 2, 3, 3, 3, 2]))
    print(filter_not_in_case_insensitive(
        ['Apple', 'banana', 'Cherry'], ['BANANA', 'pear']))
    print(future_value(1000, 0.05, 3))
