class ContactList(list):
    def search(self, name):
        '''Return all contacts that contain the search value
        in their name.'''
        matching_contacts = []
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
        return matching_contacts
class contacts:
    all_contacts = ContactList()
    def __init__(self,name,email,**kwargs):
        self.name=name
        self.email=email
        super().__init__(**kwargs)
        contacts.all_contacts.append(self)
class suplaier(contacts) :
    def order(self,order):
        return f"this is a real system i will order {order} from {self.name}" 
class AddressHolder:
    def __init__(self, street="", city="", state="", zip_code="", **kwargs):
            self.street = street
            self.city = city
            self.state = state
            self.zip_code = zip_code
            super().__init__(**kwargs)
class FriendContacts(contacts,AddressHolder):
    def __init__(self ,phone=" " ,**kwargs):
        super().__init__(**kwargs)
        self.phone=phone
frind = FriendContacts(
    name="mohamed",
    email="mohamed@gmail",
    phone="0121215894",
    street="alsakalaa",
    city="hurghada",
    state="Redsea",
    zip_code="132"
)
print (frind.__dict__)
