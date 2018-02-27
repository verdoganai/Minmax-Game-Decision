def startposition(number):
   return (int(number), 'max')


def terminalstate(state):
    if state == (0, 'min') or state == (0, 'max'):
        return True
    else:
        return False


def minimax(state, a, b):
    turn,heap=state
    if terminalstate(state):
        return utilitystatic(state)
    else:
        if heap == 'min':
            value = 250
            for x in successorsgenerator(state):
                value = min(value, minimax(x, a, b))
                b = min(b,value)
                if b <= a:
                    break
        elif heap == 'max':
            value = -250
            for x in successorsgenerator(state):
                value = max(value, minimax(x, a, b))
                a = max(a, value)
                if b<=a:
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


def decision(state):
    compare={'max': max, 'min': min}
    lastgeneration = successorsgenerator(state)
    lastgenerationutilies= [minimax(x, -250, 250) for x  in lastgeneration]
    combined= list(zip(lastgeneration, lastgenerationutilies))
    calledfunction=compare[state[1]]
    result = calledfunction(combined,key=lambda item:item[1])
    result = state[0]-result[0][0]
    return (result)


print('Game begins')
stick = input('determine stick numbers:')
stick = startposition(stick)

while True:
    player = int(input('choose a stick between 1-3:'))
    stick=list(stick)
    if player in range(1,4) and player<=stick[0]:
        if stick[0] == player:
            print('player won')
            break
        stick[0] = stick[0] - player
        print('remained sticks:', stick)
        airesult = decision(stick)
        print('AI chose:', airesult)
        stick[0] = stick[0] - airesult
        print('remained sticks:', stick)
        if stick[0]==0:
            print('AI won')
            break







