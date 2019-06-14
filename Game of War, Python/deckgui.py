"""
Author: Ken Lambert
File: deckgui.py
Project 9

Pops up a window that allows the user to view each card by pressing 
a button.  After the last card is drawn, the backside of the deck 
is displayed.
"""

from breezypythongui import EasyFrame

from tkinter import PhotoImage

from cards import Card, Deck

class DeckGUI(EasyFrame):

   def __init__(self):
      EasyFrame.__init__(self, title = "Testing a Deck Display")
      self.setSize(300, 150)
      self.deck = Deck()
      self.card = self.deck.deal()
      self.image = PhotoImage(file = self.card.fileName)
      self.cardImageLabel = self.addLabel("", row = 0, column = 0,
                                          rowspan = 3)
      self.cardImageLabel["image"] = self.image
      self.cardNameLabel = self.addLabel(row = 3, column = 0,
                                         text = self.card)
      self.button = self.addButton(row = 0, column = 1,
                                   text = "Next Card",
                                   command = self.nextCard)
      self.shuffleButton = self.addButton(row = 1, column = 1, 
                                  text = "Shuffle",
                                  command = self.shuffle)
      self.newDeck = self.addButton(row = 2, column = 1,
                            text = "New Deck",
                            command = self.new)

   def nextCard(self):
      """Deals a card from the deck and displays it,
      or displays the back side if empty."""
      if len(self.deck) == 0:
         self.image = PhotoImage(file = Card.BACK_NAME)
         self.cardNameLabel["text"] = 'Empty'     
      else:   
         self.card = self.deck.deal()
         self.image = PhotoImage(file = self.card.fileName)
         self.cardNameLabel["text"] = self.card
      self.cardImageLabel["image"] = self.image

   def shuffle(self):
      self.deck.shuffle()

   def new(self):
      """Returns the program to its initial state."""
      self.deck = Deck()
      self.cardImageLabel["image"] = self.image
      self.cardNameLabel["text"] = ""

def main():
   app = DeckGUI()
   app.mainloop()

if __name__ == "__main__":
   main()
