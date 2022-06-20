#!/usr/bin/python3
"""RZFeeser | Alta3 Research
   Printing dictionary data stored as lists to the screen
   End-of-day challege to read out of memory and display"""

import yaml
import crayons


def main():
    """On this farm there was a..."""
    # this is the data we want to loop across
    # it is a list containing 3 dictionaries
    with open('farms.yaml', 'r') as farmfile:
        farms = yaml.safe_load(farmfile)
    
    farmcount = 0
    # each time through the loop
    # farm will be equal to one of the dict within the list "farms"
    for farm in farms:
        farmcount = farmcount + 1
        print(crayons.yellow("The farm name is: " + farm.get('name') + " and they raise:"))
        for agri in farm.get('agriculture'):
            print(crayons.blue(f" - {agri}", bold=True))
    print(crayons.green("Old Mac has " + str(farmcount) + " farms."))

# Calling the main function
main()
