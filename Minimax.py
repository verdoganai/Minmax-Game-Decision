def startposition(number):
    return (int(number), 'max')


def terminalstate(state):
    if state == (0, 'min') or state == (0, 'max'):
        return True
    else:
        return False


def minimax(state, a, b):
    heap, turn = state
    if terminalstate(state):
        return utilitystatic(state)
    else:
        if turn == 'min':
            value = 250
            for x in successorsgenerator(state):
                value = min(value, minimax(x, a, b))
                b = min(b, value)
                if b <= a:
                    break
        elif turn == 'max':
            value = -250
            for x in successorsgenerator(state):
                value = max(value, minimax(x, a, b))
                a = max(a, value)
                if b <= a:
                    break
    result = state, value
    return value


def utilitystatic(state):
    assert terminalstate(state)
    if state[1] == 'max':
        return -100
    elif state[1] == 'min':
        return 100
    assert False


def successorsgenerator(state):
    successors = []
    state = toggle(state)
    newstate = decrease(state)
    i = 0
    while newstate[0] >= 0 and i < 3:
        successors.append(newstate)
        i += 1
        newstate = decrease(newstate)
    return successors


def toggle(state):
    state = list(state)
    state[1] = 'min' if state[1] == 'max' else 'max'
    state = tuple(state)
    return state


def decrease(state):
    state = state[:0] + (state[0] - 1,) + state[1:2]
    return state


def decisionmaker(state):
    compare = {'max': max, 'min': min}
    last_generation = successorsgenerator(state)
    # last_generation creates three successors e.g. [10, max] [9,max] [8,max]
    last_generation_utilies = [minimax(x, -250, 250) for x in last_generation]
    # last_generation utilites basically estimates utility values for each successor.
    combined = list(zip(last_generation, last_generation_utilies))
    # e.g. [(10, max), 100] [(9, max), 100] [(8, max), -100]
    best_selector = compare[state[1]]
    # best_selector call
    # s function from dictionary. E.g. for above situation, it calls object 'min' from (11, min)
    result = best_selector(combined, key=lambda item: item[1])
    # Since best_successor called the function to make decision of minimum values of array, it finds minimum value
    # E.g. [(10, max), 100] [(9, max), 100] [(8, max), -100] = [(8, max), -100]
    print(result)
    result = state[0] - result[0][0]
    # result gets last value by subtracting from state
    return (result)


print('Game begins')
stick = input('determine stick numbers:')
stick = startposition(stick)


while True:
    player = int(input('choose a stick between 1-3:'))
    stick = list(stick)
    if player in range(1, 4) and player <= stick[0]:
        if stick[0] == player:
            print('player won')
            break
        stick[0] = stick[0] - player
        print('remained sticks:', stick)
        airesult = decisionmaker(stick)
        print('AI chose:', airesult)
        stick[0] = stick[0] - airesult
        print('remained sticks:', stick)
        if stick[0] == 0:
            print('AI won')
            break
