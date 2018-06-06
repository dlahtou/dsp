import csv
import re
import pprint

degree_counter_dict = dict()

with open('faculty.csv') as facultyfile:
    next(facultyfile) #skip headers in line 1
    facultyreader = csv.reader(facultyfile)
    for row in facultyreader:
        degrees = row[1]
        degrees = re.sub('\.','',degrees)
        degrees = degrees.upper().strip()
        for degree in str.split(degrees):
            if degree not in degree_counter_dict:
                degree_counter_dict[degree] = 1
            else:
                degree_counter_dict[degree] += 1

pprint.pprint(degree_counter_dict)
            
