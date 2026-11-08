def names_extractor():
    with open('emails.txt', 'r') as f:
        emails = f.read().split('\n')

    with open('employees.tsv', 'w') as f:
        header = "Name\tSurname\tEmail\n"
        f.write(header)

        for email in emails:
            if email:
                names, domain = email.split('@')
                name, surname = names.split('.')

                name = name.capitalize()
                surname = surname.capitalize()
                
                row = f"{name}\t{surname}\t{email}\n"

                f.write(row)

if __name__ == '__main__':
    names_extractor()