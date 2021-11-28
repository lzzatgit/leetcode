def quicksort(nums, low, high):
    if low >= high:
        return
    p = partition(nums, low, high)

    quicksort(nums, low, p-1)
    quicksort(nums, p+1, high)


def partition(nums, low, high):
    pivot = nums[high]
    i = low - 1

    for j in range(low, high):
        if nums[j] < pivot:
            i += 1 #先把i增大一个 因为增大前i到j之间的ele都比pivot大所以增加之后nums[i]比pivot大了
            nums[i], nums[j] = nums[j], nums[i] #然后再swap

    nums[i+1], nums[high] = nums[high], nums[i+1]

    return i + 1

nums = [3, 4, 2, 0, 1]
quicksort(nums, 0, len(nums)-1)
print(nums)

# https://www.youtube.com/watch?v=0SkOjNaO1XY
# time O(nlogn)
