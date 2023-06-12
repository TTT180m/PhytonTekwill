height=float(input("Introdu inaltimea in cm"))
weight=float(input("Introdu greutatea in kg"))
BMI=weight/ (height**2)
if BMI < 18.5:
    print("You are Underweight")
elif BMI >=18.5 and BMI<=24.9:
    print("Normal weight")
elif BMI >=25 and BMI<29.9:
    print("You are Overweight")
elif BMI>=30:
    print("You are Overweight")