# Welcome to the ANISH BMI Calculator
weight=float(input("Enter you weight in kg: "))
height=float(input("Enter you height in meters: "))

height_in_meters=height/100
BMI=weight/(height_in_meters**2)
print(BMI)

if(BMI<16):
    print("You are severely underweight"), BMI

elif(BMI>=16 and BMI<18.5):
    print("You are underweight"), BMI

elif(BMI>=18.5 and BMI<24):
    print("You ard Healthy"), BMI

elif(BMI>=25 and BMI<30):
    print("You are Overweight"), BMI

elif(BMI>=30):
    print("You are Obese"), BMI
