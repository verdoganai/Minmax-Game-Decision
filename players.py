"""
game_manager.py must be run first to play!
"""
import random
from alpha_beta import *


class Player:
    def ai_player(self, state):  # creates first successors to implement minimax algorithm.
        compare = {'max': max,
                   'min': min}
        player1 = Minimax()
        last_generation = player1.successors_generator(state)
        last_generation_utilies = [ player1.minimax(succ, float('-inf'), float('inf'), 7)
                                    for succ in last_generation
                                   ]  # e.g. [100, 95, 97, 93, 100, 92]
        combined = list(zip(last_generation, last_generation_utilies))  # e.g. [('min', (2, 3, 5), 0, 0), 92]
        # print(combined)
        best_selector = compare[state[0]]  # calls python functions; min or max to choose a move
        best_move = best_selector(combined, key=lambda item: item[1])
        # print(result)
        chosen_succ, utility = best_move
        return (chosen_succ)

    def random_player(self, state):  # choose random state from successors.
        player2 = Minimax()
        succ_list = player2.successors_generator(state)
        random_move = random.randint(0, len(succ_list) - 1)
        return succ_list[random_move]

    def human_player(self, state):
        player3 = Minimax()
        succ_list = player3.successors_generator(state)
        print('Current State is:', state)
        for x, elem in enumerate(succ_list):
            print('{0}:{1}'.format(x, elem[1]))
        player_move = int(input('Choose your move number:'))
        return succ_list[player_move]

    def basic_player(self, state): # detects 1 in the successors to move. Otherwise, plays randomly.
        player4 = Minimax()
        succ_list = player4.successors_generator(state)
        for successors in succ_list:
            if 1 in successors[1]:
                return successors
        else:
            random_move = random.randint(0, len(succ_list) - 1)
            return succ_list[random_move]




