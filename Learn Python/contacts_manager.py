import contacts as co

def add(mycontacts):

    name = input('Name: ')
    phone = input('Phone: ')
    email = input('Email: ')

    entry = co.Contacts(name, phone, email)

    if name not in mycontacts:
        mycontacts[name] = entry

        print('The entry has been added.')
    else:
        print('That name already exists.')

    print("Current contacts:")
    for contact_name, contact_info in mycontacts.items():
        print(f'{contact_name}: {contact_info.phone}, {contact_info.email}')

mycontacts = {}
add(mycontacts)


def change(mycontacts):
    name = input("Enter a name: ")

    if name in mycontacts:

        phone = input("Enter the new phone number: ")
        email = input('Enter the new email address: ')

        entry = co.Contacts(name, phone, email)

        mycontacts[name] = entry

        print('Information updated')
    else:
        print('That name is not found')

mycontacts = {
    'Daniel Narh': co.Contacts('Daniel Narh', '0502317445', 'danielnarh234@gmail.com'),
    'Calista Kunge' : co.Contacts('Calista Kunge', '0203456789', 'calsitakunge789@gmail.com')
}


for contact_name, contact_info in mycontacts.items():
    print(f'{contact_name}: {contact_info.phone}, {contact_info.email}' )

change(mycontacts)
