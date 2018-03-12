from itertools import combinations

'''successors_generator includes two parts; generating sum move and collatz move.
    First, sum move has been programmed such as below codes, then collatz.'''
def successors_generator(state):
    successors = set()  # prevents same tuples.
    for x in combinations(range(len(state)), r=2):
        # creates combinations of the state;  (0,1), (0,2), (1,2)...
        # r determines length of couples.
        comb_1, comb_2 = x
        if state[comb_1] == state[comb_2]:  # checks whether same number or not
            continue
        temp = []
        for i, elem in enumerate(state):
            if i == comb_1:
                temp.append(elem + state[comb_2])
            elif i != comb_2:  # prevents to append the used numbers for summing
                temp.append(elem)
        sorted_temp = tuple(sorted(temp))  # helps to check unique valuesb by sorting
        successors.add(sorted_temp)

        # below part creates collatz move's successors
        for x in range(len(state)):
            temp = list(state)
            if state[x] % 2 == 0:
                temp[x] = int(temp[x] / 2)
            else:
                temp[x] = 3 * temp[x] + 1
            successors.add(tuple(sorted(temp)))

    return list(successors)

tup = (5, 4, 4, 3)
y = successors_generator(tup)

print(y)
