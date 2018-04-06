"""
game_manager.py must be run first to play!
"""
from functools import lru_cache as memoize
from itertools import combinations

class Minimax:
    def terminal_state(self, state, depth):
        if 1 in state[1] or depth == 0:
            return True
        else:
            return False

    @memoize(None)  # LRU cache
    def successors_generator(self, state):  # includes two parts; generating 'Capping move' and 'Collatz Ulam move'
        state = self.toggle(state)
        heap = state[1]
        successors = set()  # prevents same successors.

        # 'Capping move'
        for x in combinations(range(len(heap)), r=2):  # creates combinations; (0,1), (0,2), (1,2)...
            comb_1, comb_2 = x
            if heap[comb_1] == heap[comb_2]:  # passes same numbers.
                continue
            temp = []
            for i, stick in enumerate(heap):
                if i == comb_1:
                    total = stick + heap[comb_2]
                    total = 10 if total >= 10 else total  # we limit sum move to max 10.
                    temp.append(total)
                elif i != comb_2:  # prevents to append the used numbers in the loop.
                    temp.append(stick)
            sorted_temp = tuple(sorted(temp))  # contributes to cut-off same heaps by sorting
            successors.add(state[0:1] + (sorted_temp,) + state[2:4])

        # 'Collatz Ulam move'
        for k in range(len(heap)):
            temp = list(heap)
            if heap[k] % 2 == 0:
                divided_number = int(temp[k] / 2)
                temp[k] = divided_number
                # We append the copy of divided number to our list except '1'.
                if not divided_number == 1:
                    temp.append(divided_number)
            else:
                temp[k] = 3 * temp[k] + 1
            sorted_temp = tuple(sorted(temp))
            successors.add(state[0:1] + (sorted_temp,) + state[2:4])
        return list(successors)

    def minimax(self, state, a, b, depth):  # minimax with alpha-beta prunning and depth cut-off.
        turn, heap, max_score, min_score = state
        if self.terminal_state(state, depth):  # assigns utility values when recursion reach the terminal state.
            return self.heuristic_value(state, depth)
        else:
            if turn == 'min':
                value = float('inf')
                for successor in self.successors_generator(state):
                    value = min(value, self.minimax(successor, a, b, depth - 1))
                    b = min(b, value)
                    if b <= a: # alpha-beta prunning implementation.
                        break
            elif turn == 'max':
                value = float('-inf')
                for successor in self.successors_generator(state):
                    value = max(value, self.minimax(successor, a, b, depth - 1))  # returns with the highest value.
                    a = max(a, value)
                    if b <= a:
                        break # prun
        return value

    def toggle(self, state):  # switches states' turn
        state = list(state)
        state[0] = 'min' if state[0] == 'max' else 'max'
        state = tuple(state)
        return state

    def heuristic_value(self, state, depth):  # manhattan distance has been used for heuristic.
        assert self.terminal_state(state, depth)  # we are paranoid
        heap = state[1]
        heuristic_list = []
        for stick in heap:
            steps = 0  # heuristic counter
            if state[0] == 'max' and stick == 1:
                return -100
            elif state[0] == 'min' and stick == 1:
                return 100
            while (stick != 1):  # estimates number of steps to reach '1'
                stick = stick/2 if stick % 2 == 0 else 3 * stick + 1
                steps += 1
            heuristic_list.append(steps)
        utility_value = min(heuristic_list)
        if state[0] == 'min':
            # if it is max position, (number of steps - 100) = utility value.
            # e.g. '8'= 4, 2, 1 -> 3 (steps)-> 97 (utility)
            return (100 - utility_value)
        else:  # For min position, (100 - number of steps) = utility value.
            return (utility_value - 100)
