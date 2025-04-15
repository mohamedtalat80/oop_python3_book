import auth
import os

"""
    adding a new user to the system
    and some persissions 
    
"""
auth.authenticator.add_user("joe","joe123uy")
auth.authenticator.add_user("jane","jane123uy")
auth.autherizer.add_permission("test program")
auth.autherizer.add_permission("change program")
auth.autherizer.permit_user("joe","test program")
class Editor:
    def __init__(self):
       self.username = None
       self.menu_map = {
            "1": self.login,
            "2": self.logout,
            "3": self. ispermited,
            "4": self.change,
            "5": self.test,
            "6": self.exit_editor
        }
    def login(self):
        is_loggedin = False
        while not is_loggedin:
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            try:
               loggedin = auth.authenticator.login(username, password)
                
            except auth.InvalidUsername :
                print("Invalid username. Please try again.")
            except auth.InvalidPassword :
                print("Invalid password. Please try again.")
            else :
                self.username = username
                is_loggedin = True
                print(f"Welcome {username}!")
    def ispermited(self,permission_name):
        try:
            auth.autherizer.check_permission(self.username,permission_name)
        except auth.NotLoggedInError(self.username):
            print(f"User '{self.username}' is not logged in.")
            return False
        except auth.PermissionError(permission_name):
            print(f"Permission '{permission_name}' does not exist.")
            return False
        except auth.NotPermittedError(self.username,permission_name):
            print(f"User '{self.username}' does not have permission '{permission_name}'.")
            return False
        return True
    def logout(self):
        if auth.authenticator.logout(self.username):
            self.username = None
            return "Logged out successfully."
    def change(self):
        if self.ispermited("change program"):
            print("Changeing  program ...")
    def test(self):
        if self.ispermited("test program"):
            print("Testing program ...")
    def exit_editor(self):
        os._exit(0)
        raise SystemExit("Exiting editor...")
    def menu(self):
        while True:
            print("\nMain Menu:")
            print("1. Login")
            print("2. Logout")
            print("3. Test program")
            print("4. Change program")
            print("5. Exit")
            choice = input("Enter your choice: ")
            action = self.menu_map.get(choice)
            if action:
                action()
            else:
                print("Invalid choice. Please try again.")
if __name__ == "__main__":
    program=Editor()
    program.menu()    