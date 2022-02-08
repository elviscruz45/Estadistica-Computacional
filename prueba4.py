def square(nums):
    for i in nums:
        yield (i*i)

someNums = square([1, 2, 3, 4, 5])

print(next(someNums))
print(next(someNums))
print(next(someNums))
print(next(someNums))

# Esto imprime:
# <generator object square at 0x1004dc500>
