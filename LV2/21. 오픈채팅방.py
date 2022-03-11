# https://programmers.co.kr/learn/courses/30/lessons/42888

def solution(records):
    answer = []
    user = {}
    log = []
    
    for record in records:
        info = record.split()
        log.append((info[1], info[0]))

        if len(info) == 3:
            user[info[1]] = info[2]
#        user = ({'uid1234': 'Prodo', 'uid4567': 'Ryan'},
#        log =  [('uid1234', 'Enter'),('uid4567', 'Enter'),('uid1234', 'Leave'),('uid1234', 'Enter'),('uid4567', 'Change')])
            
    for name, action in log:
        if action == 'Enter':
            answer.append(user[name] + '님이 들어왔습니다.')
        if action == 'Leave':
            answer.append(user[name] + '님이 나갔습니다.')
            
    return answer
