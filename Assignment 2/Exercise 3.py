bio_sex = input("Enter your biological sex (M/F): ")
hemoglobin_value = int(input("Enter your hemoglobin value: "))
if bio_sex == "M":
    if 117 <= hemoglobin_value <= 150:
        print("Normal")
    elif hemoglobin_value <= 117:
        print("Low")
    else:
        print("High")
else:
    if 134 <= hemoglobin_value <= 167:
        print("Normal")
    elif hemoglobin_value <= 134:
        print("Low")
    else:
        print("High")

