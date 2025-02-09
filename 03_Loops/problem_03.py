# Problem: Print the multiplication table for a given number up to 10,
# but skip the fifth iteration.

number = int(input("Enter a Number : "))

for num in range(1*11):
    if num == 5:
        pass
    else:
        print(f"{number} * {num} = {number*num} \n ")
