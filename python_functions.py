def sum_to(num):
  sum = 0
  for n in range(1, num +1):
    sum+=n
  return sum

# print(sum_to(10))

def largest(nums):
  nums.sort()
  return nums[-1]

# print(largest([3, 5, 10]))
# print(largest([15, 5, 2]))
# print(largest([5, 12, 10]))

def occurances(str1, str2):
  adapt_str = str1.replace(str2, '')
  return (len(str1) - len(adapt_str)) // len(str2)

# print(occurances('RIP Coolio man omg', 'o'))
# print(occurances('where are my timberland boots', 'er'))

def product(*args):
  product = 1
  for arg in args:
    product *= arg
  return product

# print(product(3, 5, 12 , 4))
# print(product(3, 5, 12 ))
# print(product(3, 5))
