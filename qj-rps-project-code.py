#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

import random

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
        self.p1 = p1
        self.p2 = p2
        self.count1 = 0
        self.count2 = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"\nPlayer 1: {move1}  Player 2: {move2}")
        if self.p1.beats(move1, move2) is True:
            print(f"** PLAYER 1 WINS !! **")
            self.count1 += 1
        elif self.p2.beats(move2, move1) is True:
            print(f"** PLAYER 2 WINS !! **")
            self.count2 += 1
        else:
            print(f"** IT'S A TIE !! **")
        print(f"Score: Player 1 = {self.count1}, Player 2 = {self.count2}\n")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print(f"\nROCK-PAPER-SCISSORS - Game start!\n")
        self.count1 = 0
        self.count2 = 0
        round = 0
        while round >= 0:
            round += 1
            print(f"Round {round}:")
            self.play_round()

    def end_game(self):
        print(f"\nGame over!")
        print(f"Final Score:")
        print(f"Player 1 = {self.count1}, Player 2 = {self.count2}\n")
        if self.count1 > self.count2:
            print(f"The winner of the game was:")
            print(f"PLAYER 1 - Congratulations !!\n\n")
        elif self.count2 > self.count1:
            print(f"The winner of the game was:")
            print(f"PLAYER 2 - Congratulations !!\n\n")
        else:
            if self.count1 == 0 and self.count2 == 0:
                print(f"The game was void, as nobody won a round :(")
                print(f"Please try again!\n\n")
            else:
                print(f"The game was tied - Time for a re-match :)\n\n")
        print()
        return game.play_game()


if __name__ == '__main__':
    game = Game(Player(), HumanPlayer())
    game.play_game()
