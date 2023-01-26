

class ContactList(list):
    def search(self,name):
        matching_contacts = []
        for i in self:
            if name in i.name == name:
                matching_contacts.append(i)
        return matching_contacts

class Contact():
    all_contacts = ContactList()

    def __init__(self,name,email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)

contact1 = Contact("jon","jon@hello")
print([c.name for c in Contact.all_contacts.search("jon")])