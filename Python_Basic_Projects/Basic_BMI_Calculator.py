# Basic_BMI_Calcualtor.py
# Purpose: General Programming exercises for Python 
# Program: Basic BMI Calcualtor with If Else
PersonName="John Doe"
Height_in = 70
Weight_LB=170

BMI = 703*Weight_LB/(Height_in**2)
print("BMI: ")
print(BMI)
if BMI < 25:
    print(PersonName+" is not overweight")
else: 
    print(PersonName +" is overweight")   

# EOF:Basic_BMI_Calcualtor.py 