def binary_search(sorted_array, looking_float_num):
    low = 0
    high = len(sorted_array) - 1
    mid = 0
    iteration_counter = 0
    upper_bound = None
    while (low <= high):
        iteration_counter += 1
        mid = (high+low) // 2
        if sorted_array[mid] < looking_float_num:
            low = mid + 1
        elif sorted_array[mid] > looking_float_num:
            high = mid - 1
            upper_bound = sorted_array[mid]
        else:
            return (iteration_counter, sorted_array[mid])

    if upper_bound is None and low < len(sorted_array):
        upper_bound = sorted_array[low]

    return (iteration_counter, upper_bound)


# tests
print(binary_search(
    # expected (3, 1.017)
    sorted([1.22, 1.23, 1.11, 5.23, 10.294, 6.34, 1.06, 1.017, 1.12]), -1.13))
print(binary_search(
    # expected (4, 1.22)
    sorted([1.22, 1.23, 1.11, 5.23, 10.294, 6.34, 1.06, 1.017, 1.12]), 1.13))
print(binary_search(
    # expected (4, 1.12)
    sorted([1.22, 1.23, 1.11, 5.23, 10.294, 6.34, 1.06, 1.017, 1.12]), 1.12))
