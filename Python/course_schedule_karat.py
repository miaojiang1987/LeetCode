# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 13:59:30 2019
 给一些<course, course>代表prerequisite，只有一条可行的路径，返回中间的那节课。
eg. ("A", "C"), ("B", "D"), ("D", "A"),  ("G", "E"), ("C", "F"), ("E", "B")
唯一路径为 G->E->B->D->A->C->F
返回D
@author: Owner
"""

def course_schedule(courses):
    course_set=set()
    order=[]
    graph={}
    visit=set()
    for course in courses:
        if course[0] not in graph:
            graph[course[0]]=course[1] 
        course_set.add(course[1])

    top=""
   
    for course in courses:
        if course[0] not in course_set:
            top=course[0]

    queue=[]
    queue.append(top)
    visit.add(top)
    while queue:
        node=queue.pop()
        order.append(node)
        if node in graph and graph[node] not in visit:
            queue.append(graph[node])
            
    return order




courses=[['A','C'],['B','D'],['D','A'],['G','E'],['C','F'],['E','B']]

print(course_schedule(courses))