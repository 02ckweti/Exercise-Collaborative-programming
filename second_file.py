import random #samuel
#Robert was here!!
class Random:
    """Random function that will tell you if you guessed a number
    Attributes:
        response(int): Takes a number as a string"""
    def random_num(response):
        response = input("Pick a number!")
        if response == "5":
            return "Correct, that is the lucky number"
        else:
            return "Incorrect, wrong number"

    #Samuel
    def generate_random_number(self):
        return random.randint(1,10)
    
    #Deborah was here
    def generate_random_number(self):
        return random.randint(1,10)
