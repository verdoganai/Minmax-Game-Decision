"""
game_manager.py must be run first to play!
"""
from timeit import default_timer as timer
from players import *


def start_position():
    return ('max', (2, 3, 5, 7), 0, 0)  # turn, sticks, score of max, score of min


def increase_score(state):  # increases winner's score as 2 for terminal position.
    turn, heap, max_score, min_score = state
    if turn == 'min':
        max_score += 2
    else:
        min_score += 2
    heap = list(heap)
    heap.remove(1)
    new_state = turn, tuple(heap), max_score, min_score
    return new_state


def game_manager():
    while True:  # determines players by user.
        player_1 = int(input('Determine first player; Random(0), AI(1), Human(2) or Basic1 (3):'))
        player_2 = int(input('Determine second player; Random(0), AI(1), Human(2) or Basic1 (3): '))
        if player_1 in range(0, 4) and player_2 in range(0, 4):  # checking inputs
            break
        else:
            print('Out of range. Please choose a player')

    game = Player()
    players = [game.random_player, game.ai_player, game.human_player, game.basic_player]
    chosen_players = [players[player_1], players[player_2]]  # collecting chosen players to create a turn switcher.
    first_player, _ = chosen_players[0].__name__.split('_')
    second_player, _ = chosen_players[1].__name__.split('_')
    players_names = [first_player, second_player]  # collecting chosen players' names to illustrate whose turn.
    print(first_player + " vs " + second_player + " have been chosen.")
    return chosen_players, players_names


def export_data(duration, max_score, min_score):
    print('Score: {0} {1} duration: {2} second'.format(max_score, min_score, time_result))
    initial_state = start_position()  # we coppied starting position to export heap value.
    with open('Time Analysing.txt', 'a') as f:  # export results
        print(duration, max_score, min_score, initial_state[1], file=f)


chosen_players, players_names = game_manager()

state = start_position()
start = timer()
move_counter, turn_switcher = (0, 0)  # move counter
while (move_counter < 200):  # maximum move limit
    print('%d:' % (turn_switcher + 1) + players_names[turn_switcher] + " player's move:")
    move = chosen_players[turn_switcher](state)
    if 1 in move[1]:  # checking whether terminal state or not
        state = increase_score(move)
    else:
        state = move
    print(state)
    move_counter += 1
    turn_switcher = move_counter % 2  # switching turn
    turn, heap, max_score, min_score = state
    if not heap or move_counter >= 200:  # checking whether list and move count to finish game.
        print("Game Over.")
        if max_score > min_score:
            print('First player "%s" win.' % players_names[0])
        elif min_score > max_score:
            print('Second player "%s" win.' % players_names[1])
        else:
            print('Draw!!')
        break

end = timer()
time_result = end - start
export_data(time_result, max_score, min_score)


# from statistics_nimgame import *
# For previous experiment results that are already explained in the report.
# It needs some libraries to run.
