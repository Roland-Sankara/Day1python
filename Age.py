year = int(input("Enter year of Birth:"))
Age = (2019 - year)

if Age < 18:
    print("Minor")
elif Age < 36:
    print("Youth")
elif Age >= 36: 
    print("Elder")       