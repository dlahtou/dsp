import csv
import re
import pprint

def get_dict():
    faculty_dict = dict()

    with open('faculty.csv') as facultyfile:
        next(facultyfile) #skip headers in line 1
        facultyreader = csv.reader(facultyfile)
        for row in facultyreader:
            name = str.split(row[0].strip())[-1]

            if name not in faculty_dict:
                faculty_dict[name] = []

            degrees = row[1]
            title = row[2]
            email = row[3].lower().strip()

            faculty_dict[name].append([degrees,title,email])
    
    return faculty_dict

pprint.pprint(get_dict(),indent=1)
