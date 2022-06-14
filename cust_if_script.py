#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   if, elif, else - A simple program using conditionals to make a decision."""


message = 'The book series you have requested information about is: '

# wrap connection in a float() to accept decimals as numbers
selection = float(input("Please enter a number 1 through 5?"))

# if input value was higher or equal to 25
if selection  == 5:
    message = message + 'Star Wars, family drama in a Galaxy far far away.'
elif selection == 4:
    message = message + 'Star Trek, utopian drama in our Galaxy.'
elif selection == 3:
    message = message + 'Saga of the Skolian Empire, futuristic sci-fi romance and drama.'
elif selection == 2:
    message = message + 'In Death, sex and murder in a futuristic New York.'
elif selection == 1:
    message = message + 'Harry Potter, magicial youngsters in England.'
else:
    message = message + 'Unknown... I guess you did not want to read a book series after all.'
print(message)

