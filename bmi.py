def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    #Add code here to calculate BMI
    bmi = weight/(height*height)
    if bmi < 18.5:
        print("Underweight")
    if 18.5 < bmi < 25.0:
        print("Normalweight")
    if bmi > 25.0:
        print("Overweight")
    #Add code here to display calculate BMI
    print(bmi)
calculate_bmi(weight=70, height=1.73)
