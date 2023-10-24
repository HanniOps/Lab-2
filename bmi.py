def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi = weight/(height * height)
    print("Your BMI is " + str(bmi))
    if bmi < 18.5:
        print("Under Weight")
    elif bmi > 25:
        print("Over Weight")
    else :
        print("Normal Weight")


calculate_bmi(height=1.73, weight=57)
