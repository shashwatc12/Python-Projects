# BMI_Calcualtor_Function.py
# Purpose: General Programming exercises for Python 
# Program: Basic BMI Calcualtor using function
PersonName1="John Doe"
Height_in1 = 70
Weight_LB1 =170

PersonName2="Clark Kent"
Height_in2 = 60
Weight_LB2 =160

PersonName3="Bruce Wayne"
Height_in3 = 65
Weight_LB3 =150

def BMI_Calcualtor(name,Height_in,Weight_LB):
    BMI=703 *(Weight_LB/(Height_in**2))
    print("BMI: ")
    print(BMI)
    if BMI<25:
        return name +" not overweight"
    else:
        return name +" is overweight"

Person1_BMI=BMI_Calcualtor(PersonName1,Height_in1,Weight_LB1)
Person2_BMI=BMI_Calcualtor(PersonName2,Height_in2,Weight_LB2)
Person3_BMI=BMI_Calcualtor(PersonName3,Height_in3,Weight_LB3)

print(Person1_BMI)
print(Person2_BMI)
print(Person3_BMI)


