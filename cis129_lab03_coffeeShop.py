'''This program was written for Lab 3 of my CIS intro to Computer Science Course.
It represents a fictional coffee shop and at the end of all inputs prints a "recipt"'''

from math import *  #statically imported math module into python

print('\n\
***************************************\
\n\
\nWelcome to my cafe.') # print line for format

myAmt_1 = int(input('Number of coffees bought? \n')) #variable representing taking of the coffee order input
myAmt_2 = int(input('Number of muffins bought? \n')) #variable representing taking of the muffin order input
myAmt_3 = int(input('Number of croissants bought? \n')) #variable representing taking of the croissant order input
myAmt_4 = int(input('Number of esspressos bought? \n')) #variable representing taking of the esspresso order input

myCof = 5 * myAmt_1 #variable representing price of coffee order, the amount times by price of cups of coffee
myMuf = 4 * myAmt_2 #variable representing price of muffin order, the amount times by price of muffins
myCro = 6 * myAmt_3 #variable representing price of muffin order, the amount times by price of croissants
myEss = 8 * myAmt_4 #variable representing price of muffin order, the amount times by price of esspresso
myTax = 1.06 #amount of tax being applied to transaction, I used 1.06 so as to avoid complicating the arithmetic and having to do further calculations

Total =  round(myTax * (myMuf + myCof + myCro + myEss), 2) #sum of coffee and muffin order with tax applied
yourTax= round(.06 * (myMuf + myCof + myCro + myEss), 2)

print('\n***************************************\n', # this command prints the receipt using variables/equations from the prmompts and statements found above
'\n\
\n***************************************\n
~~ My Cafe Receipt ~~\
\n',myAmt_1 ,'Coffees @ $5.00 each: $', myCof, # Displays amnt of coffee at $5 price then shows total for the category
'\n',myAmt_2,'Muffins @ $4.00 each: $', myMuf, # Displays amnt of muffins at $4 price then shows total for the category
'\n',myAmt_3,'Muffins @ $6.00 each: $', myCro, # Displays amnt of croissants at $6 price then shows total for the category
'\n',myAmt_4,'Muffins @ $8.00 each: $', myEss, # Displays amnt of esspresso at $8 price then shows total for the category
'\n\
\n6% tax: $', yourTax, # shows the subtotal of tax
'\n\
\n---------\
\nTotal: $',Total, # shows the total price of all items purchased 
'\n\
\n***************************************\
\n')
