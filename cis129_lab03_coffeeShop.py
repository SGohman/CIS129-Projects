'''This program was written for Lab 3 of my CIS intro to Computer Science Course.
It represents a fictional coffee shop and at the end of all inputs prints a "recipt"'''

from math import *  #statically imported math module into python

print('\n\
***************************************\
\n\
\nWelcome to my cafe.') 

myAmt_1 = int(input('Number of coffees bought? \n')) #variable representing and takning coffee order input
myAmt_2 = int(input('Number of muffins bought? \n')) #variable representing and taking muffin order input

myCof = 5 * myAmt_1 #variable representing price of coffee order, the amount times by price of cups of coffee
myMuf = 4 * myAmt_2 #variable representing price of muffin order, the amount times by price of muffins
myTax = 1.06 #amount of tax being applied to transaction, I used 1.06 so as to avoid complicating the arithmetic and having to do further calculations

Total =  round(myTax * (myMuf + myCof), 2) #sum of coffee and muffin order with tax applied
yourTax= round(.06 * (myMuf + myCof), 2)

print('\n***************************************\n', # this command prints the receipt using variables/equations from the prmompts and statements found above
'\n\
~~ My Cafe Receipt ~~\
\n',myAmt_1 ,'Coffees @ $5.00 each: $', myCof,
'\n',myAmt_2,'Muffins @ $4.00 each: $', myMuf,
'\n\
\n6% tax: $', yourTax,
'\n\
\n---------\
\nTotal: $',Total,
'\n\
\n***************************************\
\n')