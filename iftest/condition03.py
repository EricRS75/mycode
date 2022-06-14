#!/usr/bin/env python3
hostname = input("What value should we set for hostname?")
## Notice how the next line has changed
## here we use the str.lower() method to return a lowercase string
if hostname.lower() == "mtg":
    print("hostname matches the config")

#For some reason they want an extra comment in the code, here is the exit
print("Exiting the script")
