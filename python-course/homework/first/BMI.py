'''
Created on 24.10.2016

@author: yacoub
'''
from BMI_Validators import *
while True:
    weight = 0
    height = 0
    print ('We will count your BMI.')
    weight = int(input("Your weight in KG please !"))
    if ( validate_weight(weight)):
        print ("Invalid weight")
        print("Give a valid weight")
        continue
    height = float(input("Your height in Meter please !"))
    if(validate_height(height)):
        print ("Invalid height")
        print("Give a valid height")
        continue
    bmi = weight / (height**2)
    print("Your BMI is %s"% bmi.__str__())

    



