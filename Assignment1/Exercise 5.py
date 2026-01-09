import math
talents = float(input("Talents: "))
pounds = float(input("Pounds: "))
lots = float(input("Lots: "))
d = float(((talents*20+pounds)*32+lots)*13.3)
e = d // 1000
f = d % 1000
print ("The weight in modern units:")
print (e,"kilograms and", f,"grams")
