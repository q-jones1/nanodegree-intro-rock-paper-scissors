#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

import random

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""

class Player:
    def move(self):
        return 'void'

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
            human_move = input("To play the game, please type either: rock, paper or scissors?\nNote: To end the game and restart at any point, type 'quit'(no quotes) >")
            if human_move in moves:
                return human_move
            if human_move == 'quit':
                return game.play_game()
            #if human_move == 'quit':
            #    return 'quit'



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
        if self.p1.beats(move1, move2) == True:
            print(f"** PLAYER 1 WINS !! **")
            self.count1 += 1
        elif self.p2.beats(move2, move1) == True:
            print(f"** PLAYER 2 WINS !! **")
            self.count2 += 1
        else:
            print(f"** IT'S A TIE !! **")
        print(f"Score: Player One {self.count1}, Player Two {self.count2}\n")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print(f"\nGame start!\n")
        self.count1 = 0
        self.count2 = 0
        round = 0
        while round >= 0:
            round += 1
            print(f"Round {round}:")
            self.play_round()
        print("Game over!")
        print(f"Final Score: Player One {self.count1}, Player Two {self.count2}\n")
        if self.count1 > self.count2:
            print("The winner of the game was PLAYER 1 - Congratulations !!")
        elif self.count2 > self.count1:
            print("The winner of the game was PLAYER 2 - Congratulations !!")
        else:
            print("The game was tied - Time for a re-match :)")
        print()

if __name__ == '__main__':
    game = Game(CyclePlayer(), HumanPlayer())
    game.play_game()
