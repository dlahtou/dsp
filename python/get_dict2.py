import csv
import re
import pprint

def get_dict():
    faculty_dict = dict()

    with open('faculty.csv') as facultyfile:
        next(facultyfile) #skip headers in line 1
        facultyreader = csv.reader(facultyfile)
        for row in facultyreader:
            name = tuple(str.split(row[0].strip()))

            degrees = row[1]
            title = row[2]
            email = row[3].lower().strip()

            faculty_dict[name] = [degrees,title,email]
    
    return faculty_dict

pprint.pprint(get_dict(),indent=1)
