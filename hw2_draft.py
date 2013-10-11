# Ulises Herrera
# Evergreen Login: ...
# Computer Science Foundations
# Programming as a Way of Life
# Homework 2

###
### Problem 1
###


# DO NOT CHANGE THE FOLLOWING LINE
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


print # line blank on purpose
# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 2 solution follows:"

for i in range(2, 11):
  print 1.0/i 


###
### Problem 3
###


print # line blank on purpose
# DO NOT CHANGE THE FOLLOWING LINE
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


print # line blank on purpose
# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 4 solution follows:"

n = 10
t = 1

for i in range(1, n+1):
    t = t * i
    
print t
        
    

###
### Problem 5
###


print # line blank on purpose
# DO NOT CHANGE THE FOLLOWING LINE
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


print # line blank on purpose
# DO NOT CHANGE THE FOLLOWING LINE
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

# ... List your collaborators and other sources of help here (websites, books, etc.),
# ... as a comment (on a line starting with "#").

###
### Reflection
###

# ... Write how long this assignment took you, including doing all the readings
# ... and tutorials linked to from the homework page. Did the readings, tutorials,
# ... and lecture contain everything you needed to complete this assignment?
