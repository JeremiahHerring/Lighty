# contacts = []
# i=0

# def print_list(contacts, i):
#     #Print contacts given in a list
#     print('================== CONTACT LIST ==================')
#     print('Index   First Name            Last Name')
#     print('======  ====================  ====================')

# for i, contact in enumerate(contacts):
#     print(f'{str(i):<8}{contact[0]:<22}{contact[1]:<22}')

# def add_contact(contacts):
#     'Prompt the user to add conacts'
#     first_name = input("Enter first name: ")
#     last_name = input("Enter last name: ")

#     contacts = contacts + first_name + last_name
#     i += 1
#     return(contacts)

# def modify_contact(contacts, i):
#     '''Modify existing contacts'''

#     index_number = input("Enter the index number")
#     if index_number != range(i):
#         print("Invalid Index Number")
#         return(contacts)
    
# print_list(contacts, i)
# add_contact(contacts)

class Contacts:
    def __init__(self, contact):
        self.contact = contact
        self.contact_list = []

    def add_contact(self, contact):
        self.contact_list.append(contact)

    def modify_contact(self, contact):
        self.contact_list.remove(contact)

    
    
