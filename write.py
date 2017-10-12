import re
import sys
# how to use
# python a.py a.txt > b.txt 

file = sys.argv[1]
f = open(file, 'r')
res = ""
line_dict_uniq = dict()
for line in f.readlines():
    line = line.strip()
    if len(line) > 1 and len(line) < 30:
        line = line.lower()
        tmp = line
        line = re.sub('[^a-zA-Z]','', line)
        if line not in line_dict_uniq.keys():
            line_dict_uniq[line] = tmp

lastDict = line_dict_uniq
line_dict_uniq = sorted(line_dict_uniq.keys())

test1 = "0"
for line in line_dict_uniq:
    test2 = lastDict[line]
    if test1[0] != test2[0] :
        print "\n\n"
        print "----------------------- " + test2[0].upper() +  " -----------------------"
        print ""
    test1 = test2
    print test2

