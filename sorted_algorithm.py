"""Simple sorting algorithm implementation.

This module provides a reusable merge sort implementation that returns a
new sorted list (ascending order) without mutating the input.
"""


def merge_sort(values):
    """Return a sorted copy of ``values`` using merge sort.

    Args:
        values: Iterable of comparable items.

    Returns:
        A new list containing the sorted values in ascending order.
    """
    values = list(values)
    if len(values) <= 1:
        return values

    middle = len(values) // 2
    left = merge_sort(values[:middle])
    right = merge_sort(values[middle:])

    return _merge(left, right)


def _merge(left, right):
    """Merge two sorted lists into one sorted list."""
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    return merged


if __name__ == "__main__":
    sample = [7, 2, 9, 1, 5, 3]
    print("Original:", sample)
    print("Sorted:", merge_sort(sample))
