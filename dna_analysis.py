# Ulises Herrera
# heruli08
# Computer Science Foundations
# Programming as a Way of Life
# Homework 3 & 4: DNA analysis (Part 1 & II)

import sys

if len(sys.argv) < 2:
    print "You must supply a file name as an argument when running this program."
    sys.exit(2)

filename = sys.argv[1]

inputfile = open(filename)

seq = ""

linenum = 0

for line in inputfile:
    linenum = linenum + 1
    # if we are on the 2nd, 6th, 10th line...
    if linenum % 4 == 2:
        # Remove the newline characters from the end of the line
        line = line.rstrip()
        seq = seq + line

		
###########################################################################
### Compute statistics
###

total_count = 0
gc_count = 0
at_count = 0
a_count = 0
t_count = 0
g_count = 0
c_count = 0

for bp in seq:
    total_count = total_count + 1

    if bp == 'C':
        gc_count += 1
        c_count += 1
    elif bp == 'G':
        gc_count += 1
        g_count += 1
    
    elif bp == 'A':
        at_count += 1
        a_count += 1 
           
    elif bp == 'T':
        at_count += 1
        t_count += 1

gc_content = float(gc_count) / total_count
at_content = float(at_count) / total_count
at_gc_ratio = float(at_count) / (gc_count)
a_content = float(a_count) / total_count
c_content = float(c_count) / total_count
g_content = float(g_count) / total_count
t_content = float(t_count) / total_count
sum_total = a_count + c_count + g_count + t_count
seq_total = len(seq)

print 'GC-content:', gc_content
print 'AT-content:', at_content
print 'A count:', a_content
print 'T count:', t_content
print 'G count:', g_content
print 'C count:', c_content
print 'Sum count:', sum_total
print 'Total count:', total_count
print 'Sequence Length:', seq_total
print 'AT/GC ratio:', at_gc_ratio

if gc_content > 0.6:
    print 'GC Classification: High GC Content'
elif gc_content < 0.4:
    print 'GC Classification: Low GC Content'
else:
   print 'GC Classification: Moderate GC Content'
