import csv
import re

def unique_domains(csv_file_name):
    domain_list = set()

    with open(csv_file_name) as facultyfile:
        next(facultyfile) #skip headers in line 1
        facultyreader = csv.reader(facultyfile)
        for row in facultyreader:
            email = row[3]
            email = email.lower().strip()
            print(email)
            domain = re.search('@.*',email)
            domain_list.add(domain.group()[1:])
    
    return list(domain_list)

print(unique_domains('faculty.csv'))
