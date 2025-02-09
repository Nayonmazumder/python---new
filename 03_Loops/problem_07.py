# 7. Validate Input
# Problem: Keep asking the user for input until they enter a number
# between 1 and 10.

input_str = int(input("Please Enter a String : "))

while True:
    input_str = int(input("Please Enter a String : "))
    if 1 <= input_str <= 10:
        print(f"Yes! {input_str} here")
        break
    else:
        print("Please Enter Again !")
