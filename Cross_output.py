'''This script can deal with two file and alternate output'''

from itertools import zip_longest
file1 = open('A.mollis.txt', 'r')
file2 = open('A.ilicifolius.txt', 'r')
out_result = open('result.txt', 'w')
for line1,line2 in zip_longest(file1,file2):
    line1 = line1.strip()
    line2 = line2.strip()
    out_result.write(line1+"\n"+line2+"\n")

out_result.close()
file1.close()
file2.close()
