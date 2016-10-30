'''
Created on 24.10.2016

@author: yacoub
'''
from BMI_Validators import *
while True:
    print ('We will count your BMI.')
    weight = input("Your weight in KG please !")
    if (not validate_weight(weight)):
        print ("Invalid weight")
        break
    height = input("Your height in Meter please !")
    if(not validate_height(height)):
        print ("Invalid height")
        break
    bmi = weight / (height**2)
    print("Your BMI is %s"% bmi.__str__())

    print



