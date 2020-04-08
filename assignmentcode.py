#!/usr/bin/python


from collections import deque
import re

f = open("input.txt", "r")


m = int(f.read(1))


f.read(1)


n = int(f.read(1))


f.read(1)


t = int(f.read(1))


f.read(3)


states = []
i = 0
while i < m:
    states.append(f.readline())
    i = i+1


filteredStates = []
i = 0 
while i < m:
    test = re.split(r'[^\w]', states[i])
    filteredStates.append(filter(bool, test))
    i = i+1


f.readline()


i = 0
rules = []
while i < n:
    rules.append(f.readline().rstrip('\r\n'))
    i = i+1


f.readline()


matrix = []
i = 0
while i < m:
    matrix.append([])
    j = 0
    while j < n:
        matrix[i].append(f.read(1))
        f.read(1)
        j = j+1
    i = i+1


f.readline()


testCases = []
i = 0
while i < t:
    testCases.append(f.readline().rstrip('\r\n'))
    i += 1


filteredTestCases = []
i = 0
while i < t:
    filteredTestCases.append([])
    temp1 = testCases[i].split('\t')[0]
    temp2 = testCases[i].split('\t')[1]
    temp1 = re.split(r'[^\w]', temp1)
    temp2 = re.split(r'[^\w]', temp2)
    filteredTestCases[i].append(filter(bool, temp1))
    filteredTestCases[i].append(filter(bool, temp2))
    i += 1


f.close()




initial_states = []
goal_states = []
i = 0
while i < t:
    j = 0
    for state in filteredStates:
        if state == filteredTestCases[i][0]:
            initial_states.append(j)
        if filteredTestCases[i][1] == state:
            goal_states.append(j)
        j = j+1
    i = i+1


class Node:
    'Class for holding the state, action, and parent Node'

    def __init__(self, state, action, parent):
        self.state = state
        self.action = action
        self.parent = parent

def Solution(goal_node, rules):
    solution_stack = []

   
    while(1):
        if goal_node.parent is not None:
            solution_stack.append(int(goal_node.action))
            goal_node = goal_node.parent
        else:
            break

   
    while solution_stack:
        if len(solution_stack) > 1:
            print rules[solution_stack.pop()], "->",
        else:
            print rules[solution_stack.pop()],
    print('')



def Search_Goal(initial_states, goal_states, rules, matrix):
    frontier = deque([])
    explored_set = deque([])
    i = 0

    
    while i < t:
        frontier.clear()
        intial_node = Node(initial_states[i], -1, None)
        frontier.append(intial_node)
        explored_set.clear()
        while (1):
            if not frontier:
                break
            node_holder = frontier.popleft()

            
            if int(node_holder.state) == goal_states[i]:
                Solution(node_holder, rules)
                break
            explored_set.append(node_holder)
            j = 0

            
            while j < n:
                state_holder = matrix[int(node_holder.state)][j]
                flag = 1
                for item in explored_set:
                    if item.state == state_holder:
                        flag = 0
                for item in frontier:
                    if item.state == state_holder:
                        flag = 0
                if flag == 1:
                    frontier.append(Node(state_holder, j, node_holder))
                j = j+1
        i = i+1

Search_Goal(initial_states, goal_states, rules, matrix)
