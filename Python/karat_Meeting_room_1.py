def meeting_room1(meetings, new_meeting):
    meetings.sort()
    for i in range(len(meetings)):
        if i == 0 and new_meeting[1] <= meetings[i][1]:
            return True
        if new_meeting[0] >= meetings[i-1][1] or new_meeting[1] <= meetings[i][0]:
            return True
        if i == len(meetings) - 1 and new_meeting[0] >= meetings[i][1]:
            return True
            
    return False

def meeting_room_overlap(meetings, new_meeting):
    meetings.sort()
    available = False
    for i in range(len(meetings)):   
        if i == 0 and new_meeting[1] <= meetings[i][1]:
            available = True
        if new_meeting[0] >= meetings[i-1][1] or new_meeting[1] <= meetings[i][0]:
            available = True
        if i == len(meetings) - 1 and new_meeting[0] >= meetings[i][1]:
            available = True           
        if available == True:
            return False
    return True