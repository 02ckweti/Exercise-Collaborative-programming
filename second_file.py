
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
        
            
    
