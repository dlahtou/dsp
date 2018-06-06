import csv
import re

def emails(csv_file_name):
    email_list = []

    with open(csv_file_name) as facultyfile:
        next(facultyfile) #skip headers in line 1
        facultyreader = csv.reader(facultyfile)
        for row in facultyreader:
            email = row[3]
            email = email.lower().strip()
            email_list.append(email)
    
    return email_list

print(emails('faculty.csv'))
