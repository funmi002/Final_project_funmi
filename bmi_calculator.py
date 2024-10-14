#BMI calculator 
def calculate_bmi():
    height = float(input("Enter your height(m): "))
    weight = float(input("Enter weight(kg): "))
    bmi = weight/(height ** 2) 

    if bmi < 18.5:
        print("Underweight")
    elif bmi < 25:
        print("Normal weight")
    elif bmi < 30: 
        print("Overweight")
    else: 
        print("Obese")
    print(f"Your bmi is: {round(bmi,2)}")
