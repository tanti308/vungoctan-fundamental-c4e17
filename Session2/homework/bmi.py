a= int(input("Your height (cm)?"))
w= int(input("Your weight (kg)?"))

h= float(a/100)

bmi= float(w/h**2)
if bmi <16:
    print("Severely underweight")
elif 16<= bmi <18.5:
    print("Underweight")
elif 18.5<= bmi <25:
    print("Normal")
elif 25<= bmi <30:
    print("Overweight")
else:
    print("Obese")
