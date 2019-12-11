# -*- coding: utf-8 -*-
'''
Given an unordered list of times of day when people are busy, write a function that tells us the intervals during the day when ALL of them are available.
Sample input:
p1_meetings = [
  {"start": 1230, "end": 1300},
  {"start":  845, "end":  900},
  {"start": 1300, "end": 1500},
]
p2_meetings = [
  {"start":  930, "end": 1200},
  {"start": 1600, "end": 2359},
]
p3_meetings = [
  {"start":  845, "end":  915},
  {"start": 1515, "end": 1545},
]
schedules = [p1_meetings, p2_meetings, p3_meetings]
Expected output:
find_available_time(schedules)
=> [    0,  845 ],
    [  915,  930 ],
    [ 1200, 1230 ],
    [ 1500, 1515 ],
[ 1545, 1600 ]

'''

def meeting_room2(schedules):
    meetings=[]
    result=[]
    for s in schedules:
        for meeting in s:
            meetings.append(meeting[start],meeting[end])
    meetings.sort()
    occupied=[meetings[0]]
    for i in range(1, len(meetings)):
        # merge intervals
        if meetings[i][0] > occupied[-1][1]:
            occupied.append(meetings[i])
        else:
            occupied[-1][1] = max(occupied[-1][1], meetings[i][1])
    
    for i in range(len(occupied)-1): 
        if i == 0 and occupied[i][0] > 0:
            result.append([0, occupied[i][0]])
        result.append([occupied[i][1], occupied[i+1][0]])
    
    return result
    
    return 

