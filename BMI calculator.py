name = str(input("Enter your name: "))

Weight = int(input("Enter your weight in pounds: "))

Height = int(input("Enter your height in inches: "))

BMI = (Weight * 703) / (Height * Height)    

print(BMI)

if BMI > 0:
    if BMI < 18.5:
        print(name +", You are underweight.")
        
    elif BMI <= 24.9:
        print(name +", You are normal height.")
    elif BMI < 29.9:
        print(name +", You are over weight.")
    elif BMI < 34.9:
        print(name +", You are obese.")
    elif BMI < 39.9:
        print(name +", You are severely obese.")
    else:
        print(name +", You are morbidly obese.")
else:
    print("Enter valid input")