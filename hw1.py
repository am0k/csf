# Ulises Herrera
# heruli08
# Computer Science Foundations, Fall 2013
# Programming as a Way of Life
# Homework 1

# You may do your work by editing this file, or by typing code at the
# command line and copying it into the appropriate part of this file when
# you are done.  When you are done, running this file should compute and
# print the answers to all the problems.

import math                     # makes the math.sqrt function available

###
### Problem 1
###

print # blank line to make reading easier
print "Problem 1 solution follows:"

# To compute: (1x**2) - (5.86x) + (8.5408)
# we need to run the equation:
# (-b +/- math.sqrt(b**2 - 4*a*c)) / (2*a)
# our values are as follows:

a = 1
b = -5.86
c = 8.5408

# the discrimant tells us which of the three outcomes are possible
# for our equation, so we need to make a statement for it.

d = (b**2) - (4*a*c)  # equation for the discriminant 
 
if d < 0:         # because we cannot take the squareroot of zero
   print "This equation has no roots."
elif d == 0:    # if the discriminant is zero, the equation only has one root
       x = (-b + math.sqrt(d)) / (2*a)
       print x
else:         # a discriminant greater than zero yields two roots
    x1 = (-b + math.sqrt(d)) / (2*a)
    x2 = (-b - math.sqrt(d)) / (2*a)
    print x1, "and", x2
        
###
### Problem 2
###

print   # blank line to make reading easier
print "Problem 2 solution follows:"

import hw1_test
print hw1_test.a
print hw1_test.b
print hw1_test.c
print hw1_test.d
print hw1_test.e
print hw1_test.f

###
### Problem 3
###

print # blank line to make reading easier
print "Problem 3 solution follows:"

# first we create an equation to evaluate the expression using values from hw1_test
from hw1_test import *
bE = ((a and b) or (not c) and not (d or e or f))

print a == bE # we run "hw1_test.a" through the bE expression
print b == bE # we keep doing this for all of them
print c == bE
print d == bE
print e == bE
print f == bE

###
### Collaboration
###

# I used google.com a lot re-learn how to solve quadratic equations. 
# I also used StockOverflow to see how other people coded their programs.

# At the tutoring session today (Friday, Oct. 4, 2013), a SoS student named Josh and 
# the TA Alex helped me debugg my semantic errors with Problem 3, and reviewed my
# solution to Problem 2

###
### Reflection
###

# The readings and tutorials took me about 2 hours.

# Problem 1 took me 5 hours--although I did over analysed it and initially 
# tried to make it more complicated than the final program submited.

# Problem 2 took less than five minutes. It almost seemed too easy compared to 
# the first one.

# Problem 3 took 1.5 hours--mostly because I could not figure out the syntax errors
# that eventually became a semantic error.

# While the books, lectures, and tutorials went over very basic things
# I had to google a lot to see how small prgrams are written and designed
# as opposed to the few and small "sample" lines of coded from our books.
