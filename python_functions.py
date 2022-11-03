def sum_to(num):
  sum = 0
  for n in range(1, num +1):
    sum+=n
  return sum

# print(sum_to(10))

def largest(nums):
  nums.sort()
  return nums[-1]

print(largest([3, 5, 10]))
print(largest([15, 5, 2]))
print(largest([5, 12, 10]))