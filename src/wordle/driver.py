
from src.wordle import wordle as wordle

class Driver():

    """
    Driver Class

    Implements run function which executes multiple functions in the list_exercises folder.

    TODO:
        Set up a dictionary to control which function gets executed and which functions get bypassed.
    """
    def __init__(self, root):
        self.root = root
        pass

    def run(self):
        word_driver = wordle.wordle(self.root)
        word_driver.play()
