#!/usr/bin/env python3
# Jeff Bohn
# 9/10/2024
# Week_4_Lab_1 
# Chapter 7 - file I/O
# main.py
################## EXERCISE_7-1 ##################

import csv

def displayErrorMessage():
    return print("Entry must be greater than zero. Please try again.\n")


def get_miles_driven():
    while True:
        miles_driven = float(input("Enter miles driven:\t"))
        if(miles_driven > 0):                               
            return miles_driven
        else:
            displayErrorMessage()
            
          
def get_gallons_used():
    while True: 
        gallons_used = float(input("Enter gallons of gas:\t"))                   
        if(gallons_used > 0):                           
            return gallons_used
        else:
            displayErrorMessage()
 
            
def writeCSV(miles_driven, gallons_used, mpg):
    numberList = [[miles_driven, gallons_used, mpg]]
    with open("mpg.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(numberList)

            
def main():
    
    print("The Miles Per Gallon program\n")

    more = "y"
    while more.lower() == "y":
        miles_driven = get_miles_driven()
        gallons_used = get_gallons_used()                                
        mpg = round((miles_driven / gallons_used), 2)

        writeCSV(miles_driven, gallons_used, float(mpg))
        
        print(f"Miles Per Gallon:\t{mpg}\n")
        
        more = input("More entries? (y or n): ")
    
    print("Bye!")

if __name__ == "__main__":
    main()
















