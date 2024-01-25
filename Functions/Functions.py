#!/bin/python3

#Programmer: Sullivan Abegg
#Program: Functions
#Date: 1.19.2024

def nl(): #New Line Function
	print('\n')


def who_am_i():	 #This is a function without parameters
	name = "Sully" #local Variable
	age = 1765
	print("My name is",name,"and I am",age,"years old.")
	
who_am_i()

nl()

def add_one_hundred(num): #num is a Parameter
	print(num + 100)


add_one_hundred(10) #16 is the Argument which inserts itself into the Parameters

nl() 

def add(x,y):
	print(x * y)
	nl()
	print(x + y)
add(5,7)

