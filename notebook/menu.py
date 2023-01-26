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
    
    