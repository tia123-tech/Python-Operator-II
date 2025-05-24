h = float(input("enter your height"))
w = float(input("enter your weight"))
bmi = w/(h**2)
print(bmi)
if bmi<= 18.4:
    print("you are underweight")
elif bmi<= 24.9:
    print("you are healthy")
elif bmi<= 29.9:
    print("you are over weight")
elif bmi<= 34.9:
    print("you are obese")
else:
    print("you are severly obese")