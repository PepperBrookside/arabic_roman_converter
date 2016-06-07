import math

# Asks for a positive integer that will be converted into roman numerals
n = int(input("Please enter an integer here: "))

# Two lists parallel with each other in equivalence
arabicList = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
romanList = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

# String variable that will be used to store the roman numeral
roman = ""

# While loop to iterate through n until 0
while n > 0:
    # Iterates simultaneously through lists of arabic and roman numerals
    for (i, j) in zip(arabicList, romanList):
        if n >= i:
            # Repeats base-10 roman numerals, if necessary
            if (math.log10(i)).is_integer():
                while n >= i:
                    roman += j
                    n = n - i
            else:
                # Adds roman numeral to string variable, subtracts value from integer variable
                roman += j
                n = n - i

# After the while loop ends we print the result
print(roman)