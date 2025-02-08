# Problem: Movie tickets are priced based
# on age: $12 for adults (18 and over), $8 for children.
# Everyone gets a $2 discount on Wednesday.
age = int(input("Please Input Your age: "))
IsWed_day = True
price = 12 if age >= 18 else 8

if IsWed_day:
    price -= 2
    print(price)
else:
    print(price)
