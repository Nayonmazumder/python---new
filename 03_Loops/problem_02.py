# 2. Sum of Even Numbers
# Problem: Calculate the sum of even numbers up to a given number n.

num = int(input("Please Enter a number : "))
sum = 0

for nums in range(num+1):
    if nums % 2 == 0:
        sum += nums

print(sum)
