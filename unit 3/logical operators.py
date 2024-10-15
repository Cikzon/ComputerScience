# logical operators
# arithmetic operators + - * /
#comparison operators > < <= => ==
# logical operators and or !
#and means both conditions must be true
#or means one of the conditions must be true
# ! (not) means the invrse, ex. ! = (not equal to)
def check_eligibility(age, exp):
    if age >=18 and exp >=1:
        print("you are eligible!")

    else:
        print("your not eligible")