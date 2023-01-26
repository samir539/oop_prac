import datetime

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
        search for a memo in both the memo contents and in the tags
        """
        return search_filters in self.memo or search_filters in self.tags
    

    
