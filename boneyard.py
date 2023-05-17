from domino import *
import random

class Boneyard:
    """This class represents a 'deck' of dominos"""

    def __init__(self, max_dots=12):
        """Creates a list of dominos from 0, 0 up to and including maxDots, maxDots"""
        self.__dominos = []
        for i in range(max_dots + 1):
            for j in range(i, max_dots + 1):
                self.__dominos.append(Domino(i, j))

    def shuffle(self):
        """Shuffles the list of dominos"""
        random.shuffle(self.__dominos)

    @property
    def is_empty(self):
        """Determines when the list of dominos is empty"""
        return len(self.__dominos) == 0

    @property
    def dominos_remaining(self):
        """Returns the number of dominos remaining in the list"""
        return len(self.__dominos)

    def draw(self):
        """Returns the 'top' domino in the boneyard. Removes the domino from the list"""
        if self.is_empty:
            return None
        return self.__dominos.pop()

    def __getitem__(self, item):
        """Allows a programmer to use [] to peek at a domino in the middle of the boneyard"""
        return self.__dominos[item]

    def __str__(self):
        """Creates a string representation of the boneyard"""
        return f"Boneyard({len(self.__dominos)} dominos remaining)"