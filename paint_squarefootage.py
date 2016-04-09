# Dustin Titus
# 4/17/15
# This program is designed to calculate the volume, surface area, cost, paint and
# flooring amounts requirements for a rectangular room of a given dimension.

import math
print("Hello, this program will help calculate the cost and ammount of paint and")
print("flooring required for a rectangular room of a given size.")

# Input section - gets room dimensions, as well as paint and flooring prices from
# the user.

print()
length = float(input("Please enter a length in feet. "))
width = float(input("Please enter a width in feet. "))
height = float(input("Please enter a height in feet. "))
paintPrice = float(input("Please enter the price of a gallon of paint. $"))
floorPrice = float(input("Please enter the price of one square foot of flooring. $"))

# Processing section - This section does all of the calculations.

volume = length*width*height
perimeter = 4*(length+width)
floor = math.ceil(length*width)
ceiling = length*width
floorCost = floor*floorPrice
roomSize = ceiling+1.8*(width*height+length*height)#This comes from subtracting
# windows and floor from the surface area formula.
paintGallons = math.ceil(roomSize/350)
paintCost = paintGallons*paintPrice


# Output section - This section tell the user all of their own inputs, and
# displays the dimensions, and costs.

print()
print()
print("The length of the room is:",length,"ft.")
print("The width of the room is:",width,"ft.")
print("The height of the room is:",height,"ft.")
print("The total room volume is:",format(volume, '.1f'),"cu. ft.")
print("The total amount of trim needed is:",perimeter,"ft")
print("The amount flooring needed is:",floor,"sq. ft.")
print("The cost of flooring will be: $",format(floorCost, '.2f'))
print("The surface area of the room, with windows is:",roomSize,"sq. ft.")
print("The room will require",paintGallons,"gallons of paint.")
print("The cost of paint will be: $",format(paintCost, '.2f'))

# Test cases, produced by the program and confirmed by hand:
#
# Case 1:
# 10*10*10 room, paint cost $25, floor $1.
# vol = 1000 cu ft, floor = 100 sq ft, floor cost = $100, total surface area is 460 sq ft
# 460/350 rounds up to 2 gal of paint, 2*25 = $50 in paint cost.
#
#Case 2:
# 20.5*15.5*10 room, paint cost $35.50, floor $2.50.
# vol = 3177.5 cu ft, floor = 317.75 rounded to 318 sq ft, floor cost = $795
# Surface area = 965.75 sq ft, 965.75/350 = 2.75 => 3, 3*35.50 = 106.5
#
# Report:
#
# To start this assignment, first I tried to figure out some of the more basic
# calculations. Then I wrote the input section, and some of the basic
# outputs, to get a basic framework in place.
#
# Once the input and output section were working, I had some adjustments to do
# on my processing section.  In testing, I worked out the more precise formatting
# as well as which calculations were off.  In one instance I noticed that my 
# paintCost was calculating from the unrounded value, so I had to go back and round
# sooner.
#
# I learned a lot about formatting numbers in this assignment. I also learned
# that you can't use any math functions on the left side of a variable declaration.
# I think in the future I might read the chapter a bit more thoroughly before
# starting to code.


