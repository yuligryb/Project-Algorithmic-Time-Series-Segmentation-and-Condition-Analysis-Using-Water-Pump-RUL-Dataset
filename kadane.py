def kadane_algorithm(arr):

    max_sum = arr[0]
    current = arr[0]

    start = end = temp = 0

    for i in range(1, len(arr)):

        if arr[i] > current + arr[i]:
            current = arr[i]
            temp = i
        else:
            current += arr[i]

        if current > max_sum:
            max_sum = current
            start = temp
            end = i

    return start, end, max_sum