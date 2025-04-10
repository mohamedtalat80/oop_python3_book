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
    def __init__(self,name,email):
        self.name=name
        self.email=email
        contacts.all_contacts.append(self)
class suplaier(contacts) :
    def order(self,order):
        return f"this is a real system i will order {order} from {self.name}" 
    class AddressHolder:
        def __init__(self,street, city, state, zip_code):
            self.street = street
            self.city = city
            self.state = state
            self.zip_code = zip_code