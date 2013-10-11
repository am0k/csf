# Ulises Herrera
# heruli08
# Computer Science Foundations
# Programming as a Way of Life
# Homework 2

###
### Problem 1
###


print "Problem 1 solution follows:"

from hw2_test import n

x = 1
a = 0

while (x <= n): 
    a = a + x
    x = x + 1
    
print a 


###
### Problem 2
###


print # blank line on purpose
print "Problem 2 solution follows:"

for i in range(2, 11):
  print 1.0/i 


###
### Problem 3
###


print # blank line on purpose
print "Problem 3 solution follows:"

n = 10
triangular_loop = 0
triangular_formula = n*(n+1)/2

for i in range(triangular_loop, n+1):
    triangular_loop = triangular_loop + i
print "Triangular number", n, "via loop:", triangular_loop
print "Triangular number", n, "via formula:", n*(n+1)/2


###
### Problem 4
###


print # blank line on purpose
print "Problem 4 solution follows:"

n = 10
t = 1

for i in range(1, n+1):
    t = t * i
    
print t
        
    

###
### Problem 5
###


print # blank line on purpose
print "Problem 5 solution follows:"

n = 10
z = 1

for i in range(1, n+1):
    z = z * i

for i in range(n, 0, -1):
    print z
    z = z / i


###
### Problem 6
###


print # blank line on purpose
print "Problem 6 solution follows:"

n = 10
z = 1

for i in range(1, n+1):
    f = 1
    for j in range(1, i+1):
        f = j * f
    
    z = z + (1.0/f)
    
print z
    
    
    
###
### Collaboration
###

# I used http://docs.python.org and http://stackoverflow.com a lot, in addition to help from tutors Alex and Kahea.

###
### Reflection
###

# The readings took me two hours, and the six problems took me five hours. 

# While the readings and lecture helped me grasp the basic concepts behind the homework, it took a lot of research
# to come up with code on my own. Even though the tutors helped a lot and the hw2.py files runs and outputs the 
# correct answers, I don’t completely understand exactly what the computer is doing with all the code. 

# I get the algorithms, but I’m not sure how the computer interprets them. 
