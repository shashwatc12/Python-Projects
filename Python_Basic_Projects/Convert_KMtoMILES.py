# Convert_KMTOMiles.py
# Purpose: General Programming exercises for Python 
# Program: Convert Kilometers to miles
KM=100
print("Initial Vlaue in KM"+ str(KM))
def convertToMiles(x):
    return 1.6*x
KMTOMILES = convertToMiles(KM)
print("The vlue of "+str(KM)+" Kms in miles is "+ str(KMTOMILES)+" Miles")
print("Please enter the value in KM to convert into Miles :")

X=int(input())
KMTOMILES=convertToMiles(X)
print("The vlue of "+str(X)+" Kms in miles is "+ str(KMTOMILES)+" Miles")
