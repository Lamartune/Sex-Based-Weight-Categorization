# /*
#  * * DO NOT ALTER OR REMOVE COPYRIGHT NOTICES OR THIS FILE HEADER.
#  * *
#  * * Copyright (C) 2023 Fatih Tün - All Rights Reserved
#  * *
#  * * Unauthorized copying of this file, via any medium is strictly prohibited
#  * *
#  * * Proprietary and confidental.
#  * *
#  * * Written by Fatih TÜN <tunbusiness1@gmail.com>, April 2023
#  */



# This program takes in a person's sex and weight as inputs and categorizes the weight as normal, below average, or above average based on the provided criteria.

sex = input("Enter sex (m/f): ")  # Ask the user to input their sex (either 'm' or 'f') and store the input in the variable 'sex'.
weight = float(input("Enter weight in kg: "))  # Ask the user to input their weight in kilograms and store the input as a floating-point number in the variable 'weight'.

# Check the sex of the person and determine the appropriate weight category based on the criteria provided.
if sex == "f":  # If the sex is female:
    if weight <= 50:  # If the weight is less than or equal to 50 kg:
        print("Weight is thin")  # Print "Weight is thin".
    elif weight <= 70:  # Otherwise, if the weight is less than or equal to 70 kg:
        print("Weight is normal")  # Print "Weight is normal".
    elif weight <= 100:  # Otherwise, if the weight is less than or equal to 100 kg:
        print("Weight is heavy")  # Print "Weight is heavy".
    else:  # Otherwise (if the weight is greater than 100 kg):
        print("Weight is obese")  # Print "Weight is obese".
elif sex == "m":  # Otherwise (if the sex is male):
    if weight <= 60:  # If the weight is less than or equal to 60 kg:
        print("Weight is thin")  # Print "Weight is thin".
    elif weight <= 80:  # Otherwise, if the weight is less than or equal to 80 kg:
        print("Weight is normal")  # Print "Weight is normal".
    elif weight <= 100:  # Otherwise, if the weight is less than or equal to 100 kg:
        print("Weight is heavy")  # Print "Weight is heavy".
    else:  # Otherwise (if the weight is greater than 100 kg):
        print("Weight is obese")  # Print "Weight is obese".
else:  # Otherwise (if an invalid sex is entered):
    print("Invalid sex entered.")  # Print "Invalid sex entered.".
