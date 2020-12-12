"""
>>> longest_subarray([7,1,1,2,0,0,3,4,1,1,0,0,0,0], 3)
4

"""

def longest_subarray(arr, threshold):
    left = 0
    right = 0
    running_sum = arr[left]

    best_result = 0
    while right < len(arr) - 1:
        while right < len(arr) - 1:
            if running_sum + arr[right + 1] <= threshold:
                right += 1
                running_sum += arr[right]
            else:
                break

        best_result = max(best_result, right - left + 1)

        running_sum -= arr[left]
        left += 1

    return best_result





