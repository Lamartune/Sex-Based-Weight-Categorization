# Sex-Based-Weight-Categorization
<mark>
Categorize weight as normal, below average, or above average based on criteria for females (0-50 kg thin, 51-70 kg normal, 71-100 kg heavy, >100 kg obese) and males (0-60 kg thin, 61-80 kg normal, 81-100 kg heavy, >110 kg obese) by inputting sex and weight. Program uses if-else statements to determine appropriate category.
</mark>
</br>
<h1>Explanation</h1>
<p>This Python code takes in two inputs from the user: the person's sex and their weight in kilograms. It then uses if-else statements to categorize the person's weight as thin, normal, heavy, or obese, based on the sex and weight criteria provided in the code.

If the person's sex is "f" for female, the code checks their weight against the female weight criteria: a weight of 0-50 kg is considered thin, 51-70 kg is normal, 71-100 kg is heavy, and above 100 kg is obese. If the person's weight falls within any of these ranges, the code prints a message indicating their weight category.

If the person's sex is "m" for male, the code checks their weight against the male weight criteria: a weight of 0-60 kg is considered thin, 61-80 kg is normal, 81-100 kg is heavy, and above 110 kg is obese. If the person's weight falls within any of these ranges, the code prints a message indicating their weight category.

If the person enters an invalid sex, the code prints a message indicating that an invalid sex was entered. The code uses the float() function to ensure that the weight input is treated as a decimal number, since weight can include decimal values.</p>
<h1>Documentation</h1>
<code>
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
</code>
