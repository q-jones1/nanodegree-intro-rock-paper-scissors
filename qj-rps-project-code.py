#!/usr/bin/env python3
# Date: 05-01-19
# This code uses the native 'random' module + free 'colored' module from pypi.
# Details are at this link: https://pypi.org/project/colored/#description
# and thus can be installed via PIP.


"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

import random
from colored import fg, bg, attr

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self):
        return 'rock'

    def beats(self, one, two):
        return ((one == 'rock' and two == 'scissors') or
                (one == 'scissors' and two == 'paper') or
                (one == 'paper' and two == 'rock'))

    def learn(self, my_move, their_move):
        pass


class CyclePlayer(Player):
    def __init__(self):
        self.my_move = 'rock'
        self.next_move = 0

    def move(self):
        for index in range(len(moves)):
            if self.next_move > 2:
                self.next_move = 0
            else:
                return moves[self.next_move]

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.next_move += 1


class HumanPlayer(Player):
    def move(self):
        while True:
            print("To play, type either: rock, paper or scissors?")
            print("Note:")
            human_move = input("To end the game, type 'quit'(no quotes) >")
            if human_move in moves:
                return human_move
            if human_move == 'quit':
                return game.end_game()

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):
    def move(self):
        random_move = random.choice(moves)
        return random_move

    def learn(self, my_move, their_move):
        pass


class ReflectPlayer(Player):
    def __init__(self):
        self.their_move = 'rock'

    def move(self):
        return self.their_move

    def learn(self, my_move, their_move):
        self.their_move = their_move


class Game:
    def __init__(self, p1, p2):
        self.count1 = 0
        self.count2 = 0
        self.p1 = p1
        self.p2 = p2
        self.ge_color = bg('gold_3a') + fg('black')
        self.ge_style = attr('reset')
        self.gr_color = bg('black') + fg('gold_3a')
        self.gr_style = attr('reset')
        self.gt_color = bg('navy_blue') + fg('white')
        self.gt_style = attr('reset')
        self.rn_color = bg('navy_blue') + fg('white')
        self.rn_style = attr('reset')
        self.rr_color = bg('black') + fg('gold_3a')
        self.rr_style = attr('reset')

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"\nPlayer 1: {move1}  Player 2: {move2}")
        if self.p1.beats(move1, move2) is True:
            print(f"{self.rr_color}** PLAYER 1 WINS !! **{self.rr_style}")
            self.count1 += 1
        elif self.p2.beats(move2, move1) is True:
            print(f"{self.rr_color}** PLAYER 2 WINS !! **{self.rr_style}")
            self.count2 += 1
        else:
            print(f"{self.rr_color}** IT'S A TIE !! **{self.rr_style}")
        print(f"Score: Player 1 = {self.count1}, Player 2 = {self.count2}\n")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print(f"\n\t\t\t\t{self.gt_color}ROCK-PAPER-SCISSORS{self.gt_style}")
        print(f"\t\t\t\t    {self.gt_color}Game start!{self.gt_style}")
        self.count1 = 0
        self.count2 = 0
        self.round = 0
        while self.round >= 0:
            self.round += 1
            print(f"{self.rn_color} Round {self.round} {self.rn_style}:")
            self.play_round()

    def end_game(self):
        print(f"\n\t\t\t\t    {self.ge_color} Game over! {self.ge_style}")
        print(f"Final Score:")
        print(f"Player 1 = {self.count1}, Player 2 = {self.count2}\n")
        if self.count1 > self.count2:
            print(f"{self.gr_color}The winner of the game was:{self.gr_style}")
            print(f"{self.gr_color}PLAYER 1{self.gr_style}")
            print(f"{self.gr_color}Congratulations !!{self.gr_style}\n\n")
        elif self.count2 > self.count1:
            print(f"{self.gr_color}The winner of the game was:{self.gr_style}")
            print(f"{self.gr_color}PLAYER 2{self.gr_style}")
            print(f"{self.gr_color}Congratulations !!{self.gr_style}\n\n")
        else:
            if self.count1 == 0 and self.count2 == 0:
                print(f"{self.gr_color}The game was void:{self.gr_style}")
                print(f"{self.gr_color}Nobody won a round :({self.gr_style}")
                print(f"{self.gr_color}Please try again!{self.gr_style}\n\n")
            else:
                print(f"{self.gr_color}The game was tied:{self.gr_style}")
                print(f"{self.gr_color}Re-match anyone? :){self.gr_style}\n\n")
        print()
        return game.play_game()


if __name__ == '__main__':
    game = Game(HumanPlayer(), CyclePlayer())
    game.play_game()
