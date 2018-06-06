import csv
test_emails = ['happy@hap.com','boop@silly.com','cam@myemail.com']

def write_to_csv(list_of_emails):
    with open('emails.csv','w') as out_file:
        email_writer = csv.writer(out_file)
        email_writer.writerow(['list_of_emails'])
        for email in list_of_emails:
            email_writer.writerow([email])

write_to_csv(test_emails)