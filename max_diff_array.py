

def maxDifference(arr):
    result = arr[1] - arr[0]
    min_element = arr[0]

    for i in range(1, len(arr)):
        if arr[i] < min_element:
            min_element = arr[i]
        if arr[i] - min_element > result:
            result = arr[i] - min_element

    return result if result else -1

print(maxDifference([2,3,10,2,4,8,1]))
