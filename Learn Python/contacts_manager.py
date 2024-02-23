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