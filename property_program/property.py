

class Property():
    """
    A superclass for all properties
    """
    def __init__(self,square_feet,num_bedrooms,num_bathrooms):
        self.square_feet = square_feet
        self.num_bedrooms = num_bedrooms
        self.num_bathrooms = num_bathrooms

    def display(self):
        print("""
        This property has 
        =================
        1.){0} square feet
        2.){1} bedroom(s)
        3.){2} bathroom(s) 
        """.format(self.square_feet,self.num_bedrooms,self.num_bathrooms))

    def prompt_init():
        return dict(square_feet=input("Enter the square feet: "),beds=input("Enter no of bedrooms: "), baths=input("Enter number of baths"))
    prompt_init = staticmethod(prompt_init)
    



prop_1 = Property(5,5,5)
prop_1.display()
