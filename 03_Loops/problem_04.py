# Find the First Non-Repeated Character
# Problem: Given a string, find the first non-repeated character.

inputed_char = input("Please Enter a String: ")

for char in inputed_char:
    if inputed_char.count(char) == 1:
        print(char)
        break
