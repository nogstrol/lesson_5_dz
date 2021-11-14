def nums_gen(nums):
    for n in range(1, nums + 1, 2):
        yield n


nums = nums_gen(9)
print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))
