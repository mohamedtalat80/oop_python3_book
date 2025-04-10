from contact_inhertance import contacts, suplaier
class Mail_Sender:
    def send_mail(self,message):
        print(f"Sending mail to {self.email}")
        
class Emailalble(contacts,Mail_Sender):
   pass
