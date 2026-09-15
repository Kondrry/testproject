def is_even(num):
    return num % 2 == 0

def average(nums):
    if not nums:
        return 0
    return sum(nums) / len(nums)