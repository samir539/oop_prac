import datetime

memoID =  0
class Note():
    """
    Class to generate notes
    @attributes
    -----
    :memo: the memo itself 
    :creation date: the data the memo was created
    :tags: descriptor tags 

    @methods
    -----
    :match: searches for string and checks that memo is what was queried
    """
    def __init__(self,contents,tags=""):
        """
        Initialise a memo with its contents, optional tags and it is given a creation date. 
        A global id for the memo is also set
        """
        self.memo = contents
        self.tags = tags
        self.creation_date = datetime.date.today()
        global memoID
        self.id = memoID + 1

    def match(self,search_filters):
        """
        search for a term in both the memo contents and in the tags
        """
        return search_filters in self.memo or search_filters in self.tags


    
class Notebook():
    """
    class to generate notebook object which contains a list of all memos along with methods to search for memos,
    add a new memo, modify an existing memo, modify the tags
    """
    
    def __init__(self):
        self.notebook_list = []
    
    def search(self, filter_term):
        """
        search for a note in the notebook_list given a filter term
        :return: all notes that match the filter term
        """
        vals = [i for i in self.notebook_list if i.match(filter_term)]
        return vals
    
    def new_note(self,memo,tags):
        """
        add a new note to the notebook
        """
        note_to_append = Note(memo,tags)
        self.notebook_list.append(note_to_append)

    def modify_memo(self, id, contents):
        """
        find a memo with the inputted id and change the memo contents to contents
        """
        for i in self.notebook_list:
            if i.id == id:
                i.memo = contents
                break
    
    def modify_tags(self,id,new_tags):
        """
        find a memo with the inputted id and change the tags of the memo 
        """
        for i in self.notebook_list:
            if i.id == id:
                i.tags = new_tags
                break

    


    

    
