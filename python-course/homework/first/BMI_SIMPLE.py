'''
Created on 25.10.2016

@author: yacoub
'''
while True:
    print ('We will count your BMI.')
    weight = int(input("Your weight in KG please !"))
    height = float(input("Your height in Meter please !"))
    bmi = weight / (height**2)
    print("Your BMI is %1.2f"% bmi)