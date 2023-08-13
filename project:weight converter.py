user_weight = input("Weight: ")
lbs_or_kg = input("(L)bs or (K)g: ").lower()

if lbs_or_kg == "l":
    kilo = float(user_weight) * 0.45
    print(f"You are {kilo} kilos")
elif lbs_or_kg == "k":
    pounds = float(user_weight) / 0.45
    print(f"You are {pounds} pounds")