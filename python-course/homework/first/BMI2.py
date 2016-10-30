while True:
    print ('We will count your BMI.')
    weight = input("Your weight in KG please !")
    height = input("Your height in Meter please !")
    bmi = weight / (height ** 2)
    print("Your BMI is %s" % bmi.__str__())