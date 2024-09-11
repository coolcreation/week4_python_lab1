#!/usr/bin/env python3
# Jeff Bohn
# 9/10/2024
# Week_4_Lab_1 
# Chapter 7 - file I/O
# main.py
################## EXERCISE_7-2 ##################

import csv
import os

def displayErrorMessage():
    return print("Entry must be greater than zero. Please try again.")


def get_miles_driven():
    while True:
        miles_driven = float(input("\nEnter miles driven:\t"))
        if(miles_driven > 0):                               
            return miles_driven
        else:
            displayErrorMessage()
            
          
def get_gallons_used():
    while True: 
        gallons_used = float(input("Enter gallons of gas:\t"))
        print()                  
        if(gallons_used > 0):                           
            return gallons_used
        else:
            displayErrorMessage()
 
            
def writeTrips(number_list):
    with open("trips.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(number_list)


def displayValues():
    with open("trips.csv", newline="") as file:
        reader = csv.reader(file)
        print(f"Distance \t Gallons \t MPG")
        for row in reader:
            print(f"{row[0]}\t\t {row[1]}\t\t {row[2]}")


def fileChecker():
    if(os.path.isfile("./trips.csv")):
        with open("trips.csv", newline="") as file:
            reader = csv.reader(file)
            rows = map(lambda row: [row[0], row[1], row[2]], reader)
            return list(rows)   # convert to list -  can't return rows as reader is closed
                  
def main():
    number_list = []
    
    print("The Miles Per Gallon program\n")
    storedNumbers = fileChecker()

    if(storedNumbers is not None):
        print(f"Distance \t Gallons \t MPG")
        for row in storedNumbers:
            number_list.append([row[0], row[1], row[2]])
            print(f"{row[0]}\t\t {row[1]}\t\t {row[2]}")
    
    more = "y"
    while more.lower() == "y":
        miles_driven = get_miles_driven()
        gallons_used = get_gallons_used()                                
        mpg = round((miles_driven / gallons_used), 2)

        number_list.append([miles_driven, gallons_used, mpg])
        writeTrips(number_list)
        displayValues()
        
        more = input("More entries? (y or n): ")
    
    print("Bye!")

if __name__ == "__main__":
    main()















