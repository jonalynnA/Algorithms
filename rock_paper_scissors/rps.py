#!/usr/bin/python

import sys
import random


def rock_paper_scissors(number_of_players):
    global all_combinations
    all_combinations = []
    move_options = ['rock', 'paper', 'scissors']

    def build_moves(countdown, piece_being_built):
        if countdown == 0:
            all_combinations.append(piece_being_built)
            return

        for move in move_options:
            new_piece_result = piece_being_built + [move]
            build_moves(countdown - 1, new_piece_result)
    build_moves(number_of_players, [])

    return all_combinations


if __name__ == "__main__":
    num_of_people = random.randrange(6)

    if num_of_people > 1:
        num_of_people = num_of_people
        print(f"\nIf you were to play with \033[34m{num_of_people} people,\033[37m the possible combinations would be: \n\n", rock_paper_scissors(
            num_of_people))
        print("\nThat is a total of: \033[32m" +
              str(len(all_combinations)) + " combinations\n")
    else:
        print(
            f"\n\033[31mUsage: rps.py number of players was: {num_of_people}. Must be greater than 2.\n")
