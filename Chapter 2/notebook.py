import datetime 
last_id=0
class Note:
    """ the intializetion of the note class """
    def __init__(self,memo,tags =''):
        self.memo = memo
        self.tags = tags
        global last_id
        last_id+=1
        self.id = last_id
        self.created_at = datetime.datetime.today()
    def match(self, filter):
        """ the match method """
        return filter in self.memo or filter in self.tags
    
class Notebook:
    """ the notebook class """
    def __init__(self):
        self.notes = []
    # def show_notes(self):
    #     """ the shownotes method """
    #     for note in self.notes:
    #         print(f"{note.id}: {note.memo} ({note.tags}) at {note.created_at.strftime('%Y-%m-%d')}")
    def addnote(self,memo,tags=''):
        """ the addnote method """
        self.notes.append(Note(memo,tags))
    def _find_note(self,id):
        """ the findnote method """
        for note in self.notes:
            if note.id == id:
                return note
            return None

    def modify(self,id,memo,tags=""):
        """ the modify method """
        for note in self.notes:
            if note.id == id :
                self._find_note(id).memo = memo
                self._find_note(id).tags = tags
                
            break
    def search(self,filter):
        """ the search method """
        for note in self.notes:
            if note.match(filter):
                return note
        return None
    
