# Name: Anant Robinson
#Group Member: Alex Sanders
# Evergreen Login: robana07
#		     sanale04@evergreen.edu
# Computer Science Foundations
# Programming as a Way of Life
# Homework 6

# You may do your work by editing this file, or by typing code at the
# command line and copying it into the appropriate part of this file when
# you are done.  When you are done, running this file should compute and
# print the answers to all the problems.


###
### Problem 3 (Creating Dictionaries)
### Create a dictionary associated with these awesome bands and their legendary 
### lead singers. Freddy Mercury and Queen, Kurt Cobain and Nirvana, Mark Knopfler
### and Dire Straits. By the end, it should look like this:
# Lead Singers = {'Freddy Mercury' : Queen, 'Kurt Cobain' : Nirvana, 'Mark Knopfler' : Dire Straits}


# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 3 solution follows:"

Lead_Singers = {
  'Freddy Mercury':'Queen',
  'Kurt Cobain':'Nirvana',
  'Mark Knopfler':'Dire Straits'
}
print Lead_Singers


###
### Problem 4 (Assertions)
### Let's set these legendary singers to equal to 1. Now let's add Justin Bieber 
### and have him equal to 0. Assert a statement that returns a value that is less 
### than 1 that will say "Not a legendary singer, but a whiny little bitch" Print 
### out each of the singers and the statement should either be that, or "Bloody 
### amazing, have my babies?"

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 4 solution follows:"

Lead_Singer['Freddy Mercury'] = 1
Lead_Singer['Kurt Cobain'] = 1
Lead_Singer['Mark Knopfler'] = 1
Lead_Singer['Justin Bieber'] = 0

if Lead_Singer[] < 1:
        print "(Definitively) Not a legendary singer."
else:
        print "(Still not a) legendary singer."


###
### Problem 5
###Write Python code creating one of each type of data structure, using the correct 
### kind of grouping symbol (square brackets, curly braces, parentheses, and curly 
### braces with colons inside). 


# DO NOT CHANGE THE FOLLOWING LINE
#print "Problem 5 solution follows:"


Dictionary = {}
Dictionary['Tuple key'] = (a, b)
Dictionary['List key'] = ('a1', 'b1', 'c1')
Dictionary['Dictionary inside a dictionary'] = {"a" : 1 , "b" : 2 , "c" : 3}
print Dictionary

###
### Problem 6
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 6 solution follows:"


# ... write your code and comments here (and remove this line)

print There was no "Problem 6" in the file "https://github.com/robana07/csf/blob/master/hw6%20ours.txt"...


###
### Problem 7
###Now let's add more bands and singers and include them in the dictionary. 
### Billie Joe Armstrong and Greenday, Matthew Bellamy and Muse, Jimi Hendrix and 
### Band of Gypsys, John Lennon and The Beattles. Come up with a way to find out 
### if the singers are currently alive and at the end, print out alive and dead. 
### So it should be:
Print Alive
Print Dead

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 7 solution follows:"

decent_bands = {
  'Billie Joe Armstrong':'alive', 
  'Matthew Bellamy':'dead', 
  'Jimi Hendrix':'dead', 
  'John Lennon':'dead'
  }

def mortality(x):
        if decent_bands[x] == "alive":
                print "Alive"
        else:
                print "Dead"

###
### Collaboration
###

# Pythong.org, Stackoverflow, google   :)
