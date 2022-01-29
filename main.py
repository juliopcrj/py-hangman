#!/usr/bin/env python3

from random import randint
from words import words

lives = 5
class Hangman():

    def __init__(self):
        self.word = ""
        self.revealed = ""
        self.letters = ""
        self.lives = lives

    def ChooseWord(self):
        length = len(words) -1
        choice = randint(0,length)
        self.word = words[choice]
        self.revealed = [0] * len(self.word)

    def AttemptLetter(self,letter) -> int:
        if letter in self.letters:
            return 2

        self.letters += letter

        if letter not in self.word:
            return 1

        return 0

    def RevealLetter(self, letter):
        indexes = [i for i, v in enumerate(self.word) if letter == v]
        for _i in indexes:
            self.revealed[_i] = 1

    def PrintRevealed(self):
        for i,v in enumerate(self.revealed):
            if v == 1:
                print(self.word[i], sep="", end="")
            else:
                print('#', sep="", end="")
        print("")

    def run(self):
        self.ChooseWord()
        while self.lives > 0 and 0 in self.revealed:
            print(f"What you've got: ")
            self.PrintRevealed()
            _l = input("What will the letter be, stranger: ")[0]
            res = self.AttemptLetter(_l)
            if res == 0:
                print(f"Big succ, the letter {_l} is in the word.")
                self.RevealLetter(_l)
            if res == 1:
                print(f"No, this word does not contain {_l}.")
                self.lives -= 1
            if res == 2:
                print(f"You've already tried the letter {_l}, my dude.")

        if(0 not in self.revealed):
            print(f"Big day, my confederate. The word was indeed {self.word}!")
        if(self.lives <= 0):
            print(f"Little day, my dead man. The word was actually {self.word}...")


if __name__ == "__main__":
    Hangman().run()
