#!/usr/bin/python

import sys
import random


def rock_paper_scissors(number_of_people):
    global all_combinations
    all_combinations = []
    choices_for_player = ['rock', 'paper', 'scissors']

    def possible_combination(players_left, possible_combinations):
        if players_left == 0:
            all_combinations.append(possible_combinations)
            print(possible_combinations)
            print(
                players_left)
            return

        for choice in choices_for_player:
            array_of_players_throw = possible_combinations + [choice]
            possible_combination(num_of_people - 1, array_of_players_throw)
    possible_combination(number_of_people, [])

    return all_combinations


if __name__ == "__main__":
    num_of_people = random.randrange(6)

    if num_of_people > 1:
        num_of_people = num_of_people
        print(f"\nIf you were to play with \033[34m{num_of_people} people,\033[37m the possible combinations would be: \n\n", rock_paper_scissors(
            num_of_people))

    else:
        print(
            f"\n\033[31mUsage: rps.py number of plays was: {num_of_people}. Must be greater than 2.\n")
print(
    "\nThat is a total of: \033[32m" + str(len(all_combinations)) + " combinations\n")
