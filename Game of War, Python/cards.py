"""
Author: Emily Boyes
File: cards.py
Project 9

Module for playing cards, with classes Card and Deck
""" 
import random

class Card(object):
    """ A card object with a suit, rank, and file name.
    The file name refers to the card's image on disk."""

    RANKS = tuple(range(1, 14))

    SUITS = ('Spades', 'Hearts', 'Diamonds', 'Clubs')

    BACK_NAME = 'DECK/b.gif'

    def __init__(self, rank, suit):
        """Creates a card with the given rank and suit."""
        if not (rank in Card.RANKS):
            raise RuntimeError('Rank must be in ' + str(Card.RANKS))
        if not (suit in Card.SUITS):
            raise RuntimeError('Suit must be in ' + str(Card.SUITS))
        self.rank = rank
        self.suit = suit
        self.fileName = 'DECK/' + str(rank) + suit[0].lower() + '.gif'
        
    def __str__(self):
        """Returns the string representation of a card."""
        if self.rank == 1:
            rank = 'Ace'
        elif self.rank == 11:
            rank = 'Jack'
        elif self.rank == 12:
            rank = 'Queen'
        elif self.rank == 13:
            rank = 'King'
        else:
            rank = self.rank
        return str(rank) + ' of ' + self.suit

class Deck(object):
    """A deck object that allows the user to create a new deck, check the size
    of the deck, deal cards from it, ask if its empty, shuffle it, and
    obtain its string representation."""

    def __init__(self):
        """Creates a new deck of cards."""
        self.cards = []
        for suit in Card.SUITS:
                for rank in Card.RANKS:
                    c = Card(rank, suit)
                    self.cards.append(c)

    def __len__(self):
        """Returns the number of cards left in the deck."""
        return len(self.cards)

    def deal(self):
        """Removes and returns the top card or None if the deck is empty"""
        if len(self) == 0:
            return None
        else:
            return self.cards.pop(0)

    def shuffle(self):
        """Shuffles the cards."""
        random.shuffle(self.cards)

    def __str__(self):
        """Returns the string representation of a deck."""
        result = ''
        for c in self.cards:
            result = result + str(c) + '\n'
        return result

    def isEmpty(self):
        return len(self.cards) == 0
        
