def appearance(intervals):
    answer = 0
    
    #0 - таймстемпамп, 1 - роль, 2 - вход\выход(1,0) 
    events = []

    for interval in intervals:
        current_events = intervals[interval]
        for event in range(len(current_events)):
            events.append((current_events[event], interval, int(event%2==0)))
            
    events.sort()
    print(events)
    
    #0: таймстемпамп, 1 - статус действия
    last_actions = {'lesson': [0, 0], 'pupil': [0, 0], 'tutor': [0, 0]}
    
    for event in events:
        
        last_actions[event[1]] = event[0], event[2]
        
        if event[1] == 'lesson':
            if event[2] == 1:
                
                if last_actions['pupil'][0] != 0 and last_actions['pupil'][1] != 0:
                    last_actions['pupil'] = [event[0], 1]
                    
                if last_actions['tutor'][0] != 0 and last_actions['tutor'][1] != 0:
                    last_actions['tutor'] = [event[0], 1]
                        
            elif event[2] == 0:
                
                if last_actions['pupil'][1] != 0 and last_actions['tutor'][1] != 0:
                    answer += event[0] - min(last_actions['pupil'][0], last_actions['tutor'][0])
                    
                break
                
        else:
            opposite = 'pupil' if event[1] == 'tutor' else 'tutor'
            
            if event[2] == 0:
                answer +=  last_actions[event[1]][0] - last_actions[opposite][0]
            elif event[2] == 1 and last_actions[opposite][1] != 0:
                last_actions[opposite] = [event[0], 1]
                
    return answer

tests = [
    {'data': {'lesson': [1594663200, 1594666800],
             'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
             'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
    },
    {'data': {'lesson': [1594702800, 1594706400],
             'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
             'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
    'answer': 3577
    },
    {'data': {'lesson': [1594692000, 1594695600],
             'pupil': [1594692033, 1594696347],
             'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
    'answer': 3565
    },
]

if __name__ == '__main__':
   for i, test in enumerate(tests):
       test_answer = appearance(test['data'])
       print(f'{i}: {test_answer}')
       #assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
