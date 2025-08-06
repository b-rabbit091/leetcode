'''

You're given an sorted array arr of n integers and an integer x.
Find the floor and ceiling of x in arr[0..n-1].
The floor of x is the largest element in the array
which is smaller than or equal to x.
The ceiling of x is the smallest element in the array greater than or equal to x.

Example 1:
Input Format: n = 6, arr[] ={3, 4, 4, 7, 8, 10}, x= 5
Result: 4 7
Explanation: The floor of 5 in the array is 4, and the ceiling of 5 in the array is 7.
'''


def getFloorAndCeil(nums, len, target):
    low = 0
    high = len - 1

    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return [nums[mid]] * 2
        elif nums[mid] < target:
            low = mid + 1
        elif nums[mid] > target:
            high = mid - 1
    high = max(0, high)
    low = max(0, low)
    if nums[high] > target:
        return [nums[low], nums[high]]
    return [nums[high], nums[low]]


a = [3, 4, 4, 7, 8, 10]
n = 6
x = 8
print(getFloorAndCeil(a, n, x))
