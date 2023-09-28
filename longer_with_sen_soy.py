def longest(ss):
    if len(ss) < 2:
        return 'Bad sequence'
    state = {'direction': '', 'length': 0,
             'start': 0, 'end': 0,
             'the_length': 0, 'the_start': 0, 'the_end': 0}
    for i in range(1,len(ss)):
        #print(i)
        #определяем направление
        if state['direction'] == "":
            raznica = ss[i] - ss[i-1] # 1 - 0, 2 - 1, 4 - 3
            if raznica > 0:
                state['direction'] = 'возрастающая'
                state['start'] = i - 1
                state['end'] = i
                state['length'] = 1
            elif raznica < 0:
                state['direction'] = 'убывающая'
                state['start'] = i - 1
                state['end'] = i
                state['length'] = 1
            elif raznica == 0:
                state['direction'] = ""
                state['start'] = 0
                state['end'] = 0
                state['length'] = 0
        if state['direction'] != "":
            raznica = ss[i] - ss[i-1]
            if raznica > 0:
                if state['direction'] == 'возрастающая':
                    state['end'] = i
                    state['length'] += 1
                else:
                    state['direction'] = "возрастающая"
                    state['start'] = i - 1
                    state['end'] = i
                    state['length'] = 2
            elif raznica < 0:
                if state['direction'] == 'убывающая':
                    state['end'] = i
                    state['length'] += 1
                else:
                    state['direction'] = "убывающая"
                    state['start'] = i - 1
                    state['end'] = i
                    state['length'] = 2
            elif raznica == 0:
                state['direction'] = ""
                state['start'] = 0
                state['end'] = 0
                state['length'] = 0

        if state['the_length'] < state['length']:
            state['the_start'] = state['start']
            state['the_end'] = state['end']
            state['the_length'] = state['length']
        #print(state['direction'])
    return "The length:"+ str(state['the_length']) + " The start:" + str(state['the_start']) + " The end:" + str(state['the_end'])

while True:
    print('\nEnter the subsequence:\n')
    ss = input().split(' ')
    ss = [int(i) for i in ss]
    print(longest(ss))

