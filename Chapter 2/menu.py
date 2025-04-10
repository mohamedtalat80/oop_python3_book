import sys
from notebook import Notebook,Note 
class Menu:
    """ the menu class """
    def __init__(self):
        self.notebook = Notebook()
        self.choices = {
            "1": self.show_notes,
            "2": self.search_notes,
            "3": self.add_notes,
            "4": self.modify_notes,
            "5": self.quit
        }
    def display_menu(self):
        """ the display menu method """
        print(
            """
            Notebook Menu:
            1. Show all notes
            2. Search notes
            3. Add note
            4. Modify note
            5. Quit
            """
        )
    def run(self):
        """ the run method """
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")
            action = self.choices.get(choice)
            if action:
                try:
                    action()
                except Exception as e:
                    print(f"Error: {e}")
            else:
                print("Invalid choice. Please try again.")
            
    def show_notes(self,notes=None):
        """ the show notes method """
        if notes is None:
            notes = self.notebook.notes
        if not notes:
            print("No notes found.")
        else:
            for note in notes:
                print(f"{note.id}: {note.memo} ({note.tags}) at {note.created_at.strftime('%Y-%m-%d')}")
    def search_notes(self):
        filter_txt = input("Enter a filter: ")
        notes = self.notebook.search(filter_txt)
        if notes:
            self.show_notes(notes)
        else:
            print("No notes found.")
    def add_notes(self):
        memo = input("Enter a note: ")
        tags = input("Enter tags: ")
        self.notebook.addnote(memo,tags)
        print("Note added.")
    def modify_notes(self): 
        noteid = int(input("Enter the number of the note: "))
        memo = input("Enter a new note: ")
        tags = input("Enter new tags: ")
        self.notebook.modify(noteid,memo,tags)
        print("Note modified.")
    def quit(self):
        """ the quit method """
        print("Goodbye!")
        sys.exit(0) 
if __name__ == "__main__":
    # Create an instance of the Menu class and run it
    menu = Menu()
    menu.run()
