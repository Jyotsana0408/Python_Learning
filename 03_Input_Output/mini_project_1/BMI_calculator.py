"""
Body Mass Index (BMI)
"""

name = input("Please enter your name: ")
weight = float(input("Please enter your weight: "))
height = float(input("Please enter your height: "))

body_mass_index = weight/(height**2)
bmi = round(body_mass_index,2)
print("Your Body Mass Index (BMI) is: ",bmi)