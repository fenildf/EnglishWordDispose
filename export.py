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
        line = re.sub('[^a-zA-Z]','', line).lower()
        if line not in line_dict_uniq.keys():
            line_dict_uniq[line] = line

line_dict_uniq = sorted(line_dict_uniq.keys())
for line in line_dict_uniq:
    print line
