from notebook import Notebook, Note
import sys

class Menu:
    """
    A menu to use the notebook
    """
    def __init__(self):
        self.notebook = Notebook()
        self.choices = {"1": self.show_notes,"2":self.search_notes,"3":self.add_note,"4":self.modify_note,"5":self.quit}

    def display_menu(self):
        print(""" Notebook Menu
        1.Show all notes
        2.Search Notes
        3.Add Note
        4.Modify Note
        5.Quit
        """)
    
    def run(self):
        """ show menu and act on the user input"""
        while True:
            self.display_menu()
            choice = input("enter an input")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))
    
    def show_notes(self, notes=None):
        if not notes:
            notes = self.notebook.notebook_list
        for note in notes:
            print("{0}:{1}\n{2}".format(note.id,note.tags,note.memo))
    
    def search_notes(self):
        filter = input("search for:")
        notes = self.notebook.search(filter)
        self.show_notes(notes)

    def add_note(self):
        contents = input("input the note contents:")
        self.notebook.new_note(contents)
        print("note added")

    def modify_note(self):
        id = input("enter id of note you wish to modify: ")
        contents = input("enter the new contents you would like in your note:")
        self.notebook.modify_memo(id, contents)

    

