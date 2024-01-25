#!/bin/python3

#Programmer: Sullivan Abegg
#Program: Variables
#Date: 1.11.2024

quote = "Lebron James is the GOAT"
print(quote)
print(quote.upper()) #Uppercase 
print(quote.lower()) #Lower
print(quote.title()) #Title case
print(len(quote)) #counts number of characters

name = "Lebron James"
age = 39 #int
ppg = 25.7 #float

print(int(age))
print(int(ppg)) #casts a float into an int. Wont Round up

print("\nMy name is " + name + " and I am " + str(age) + " years old and averaging " + str(ppg) + " points per game.") #Concatenate variables while casting ints to strings

print("\nMy name is",name,"and I am ",age,"years old and averaging",ppg,"points per game.") #Concatenate variables while casting ints to strings using commas instead of pluses while casting our ppg variable into a string to account for the spacing before the period

print("")
age += 1 #adds 1 to variable age
print(age)

print("")
age += 10 #adds 10 the variable age
print(age)

print("")
birthday = 1 #stores 1 in the variable, Two variables can be added together as long as they are integers and not strings
age += birthday #adds 1 to the varaible age
print(age)
