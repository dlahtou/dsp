import csv
import re
import pprint

title_counter_dict = dict()

with open('faculty.csv') as facultyfile:
    next(facultyfile) #skip headers in line 1
    facultyreader = csv.reader(facultyfile)
    for row in facultyreader:
        title = row[2]
        title = title.lower().strip()
        title = str.split(title)[0]
        if title not in title_counter_dict:
            title_counter_dict[title] = 1
        else:
            title_counter_dict[title] += 1

pprint.pprint(title_counter_dict)
            
