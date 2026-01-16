import math

pizza_1 = float(input("Enter diameter for the first pizza (meter): "))
pizza_2 = float(input("Enter diameter for the second pizza (meter): "))
unit_price_1 = float(input("Enter price for the first pizza: "))
unit_price_2 = float(input("Enter price for the second pizza: "))
area_1 = (pizza_1/2) * math.pi * 2
area_2 = (pizza_2/2) * math.pi * 2
total_price_1 = unit_price_1 * area_1
total_price_2 = unit_price_2 * area_2
if total_price_1 > total_price_2:
    print("The first pizza provide better value for money")
elif total_price_1 < total_price_2:
    print("The second pizza provide better value for money")
else:
    print("Both pizzas provide the same value for money")