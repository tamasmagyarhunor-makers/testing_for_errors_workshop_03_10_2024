class Train():
    def __init__(self):
        self.colour = ''

    def set_colour(self, colour):
        if type(colour) is str:
           self.colour = colour
        else:
            raise Exception(f"{colour} is not a String. Colour should be a string")