from contact_inhertance import contacts, suplaier
''' this is over riding without super'''
class FriendContacts(contacts):
    def __init__(self ,name ,email,phone):
        self.name=name
        self.email=email
        self.phone=phone
''' this is over riding with super'''
class FriendContacts_withsuber(contacts):
    def __init__(self ,name ,email,phone):
        super().__init__(name,email)
        self.phone=phone
        