# 6. Factorial Calculator
# Problem: Compute the factorial of a number using a while loop.

fact_number = int(input("Please Enter a Number:  "))
res = 1
while fact_number > 0:
    res = res*fact_number
    fact_number -= 1
print(f"Your factorial of {fact_number} is : ", res)
