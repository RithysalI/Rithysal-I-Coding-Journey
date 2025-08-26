""
Course: CSCI 175
Assignment: 1
Author: Rithysal I.
Date: Sep 3, 2023

Description:
It is a simple application that will (roughly) calculate how many years of your life you have spent sleeping.
""

print ("Assignment 1")
print ()
name = input ("What is your name? ")
age = input ("How old are you? ")
sleep = input ("How many hours do you sleep at night? ")
wasted_years = (int(sleep) / 24) * int(age)
print ()
print ("Hello, " + name + "."
+ "\n"
+ "You have been unconscious for " + str(wasted_years) + " years!")
