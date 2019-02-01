
# coding: utf-8

# In[1]:


#implementation of function "Iterative_deepening_DFS"
import time
import numpy as np
import sys

goalState = [0, 1, 2, 3, 4, 5, 6, 7, 8]
'''results = []
iterations = []
moves = []
steps = []
timer = []
dLimit = 10''' #use at other time




class Node(object):
    def __init__(self, state, parent, operator, depth):
        self.state = state
        self.parent = parent
        self.operator = operator
        self.depth = depth
        self.left = None
        self.up = None
        self.down = None
        self.right = None 

    def DFS(self):
        start = time.time()

        que = [self] #initialization of que
        quePopper = 0 #how many pops are made
        queMaxCounter = 1 

        queNodeDepth = [0] #how deep it goes ;P
        pathCost = [0] 
        visited = [] #prevent repeated paths
        
        while que is not None: 
            if len(que) > queMaxCounter:
                queMaxCounter = len(que)
            curNode = que.pop(0)
            quePopper =+ 1

            curDepth = queNodeDepth.pop(0) #take from queue
            curPathCost = pathCost.pop(0) #initialize path cost -> use later
            visited.append(curNode.state.copy()) #adds all visited items that are unique
            
            print('Starting: ')
            print(curNode.state)
            if curNode.compState(curNode.state):
                curNode.printBoard() #check coding
                print('Time: ', str(quePopper), ' nodes popped off the queue')
                print('Space: ', str(queMaxCounter), ' nodes in the queue at its max')
                print('time spent: %0.2fs' % (time.time() - start))
                return true
            else:
                if (curNode.swapCheck(curNode.state, -1)): #expand left node
                    curNode.left = Node(curNode.doSwap(curNode.state, -1), curNode.state, 'l', curNode.depth + 1)
                    if (curNode.left.state not in visited): #store if not visited
                        que.insert(0, curNode.left)
                        queNodeDepth.insert(0, curNode.left.depth)
                        pathCost.insert(0, (curNode.state[curNode.state.index(0) - 1] + curPathCost))
                        print("L: " + str(curNode.left.state))

                if (curNode.swapCheck(curNode.state, 1)): #expand right node
                    curNode.right = Node(curNode.doSwap(curNode.state, 1), curNode.state, 'r', curNode.depth + 1)
                    if (curNode.right.state not in visited):
                        que.insert(0, curNode.right)
                        queNodeDepth.insert(0, curNode.right.depth)
                        pathCost.insert(0, (curNode.state[curNode.state.index(0) + 1] + curPathCost))
                        print("R: " + str(curNode.right.state))

                if (curNode.swapCheck(curNode.state, -3)) : #expand up node
                    curNode.up = Node(curNode.doSwap(curNode.state, -3), curNode.state, 'u', curNode.depth + 1)
                    if (curNode.up.state not in visited):
                        que.insert(0, curNode.up)
                        queNodeDepth.insert(0, curNode.up.depth)
                        pathCost.insert(0, (curNode.state[curNode.state.index(0) - 3] + curPathCost))
                        print("U: " + str(curNode.up.state))

                if (curNode.swapCheck(curNode.state, +3)): #expand down node
                    curNode.down = Node(curNode.doSwap(curNode.state, +3), curNode.state, 'd', curNode.depth + 1)
                    if (curNode.down.state not in visited):
                        que.insert(0, curNode.down)
                        queNodeDepth.insert(0, curNode.down.depth)
                        pathCost.insert(0, (curNode.state[curNode.state.index(0) + 3] + curPathCost))
                        print("D: " + str(curNode.down.state))
           
    def swapCheck(self, curState, val): #verify if able to swap
        index = curState.index(0)
        move = index + val
        if (0 <= move <= 8):
            if val == -1:#check left
                if (index != 0) & (index != 3) & (index != 6):
                    return True
            elif val == 1: #check right
                if (index != 2) & (index != 5) & (index != 8):
                    return True
            elif val == -3: #check up
                if (index != 0) & (index != 1) & (index != 2):
                    return True

            elif val == 3: #check down
                if (index != 6) & (index != 7) & (index != 8):
                    return True
        return False
    def doSwap(self, nState, val): #swap it
        copy = nState.copy()
        index = nState.index(0)
        copy[index], copy[index + val] = copy[(index + val)], copy[index]
        return copy
    def compState(self, state): #is it goals or nah?
        for i in range (9):
            if state[i] != goalState[i]:
                return False
        return True

def IDS (inState): #incomplete
    for i in range ( dLimit ):
        t = time.time()
        iterations.append(1)
        root = Node(inState, None, 'Start', 0)
        results.append(root.state)
        DFS(root, i)
        t1 = time.time() - t
        timer.append(t1) 
        

def main():
    f = open("8puz.txt", "r")
          
    for n in range(1): 
        line = f.readline().split(', ')
        line =[int(i) for i in line]
        inState = line
        rootNode = Node(inState, None, None, 0)
        rootNode.DFS()

    print("Average Steps\t" + str(np.sum(steps)))
    f.close()

main()


# # Assignment 1, 8-Puzzle Programming

# # Your homework must be implemented in this Notebook file. 
# You can add as many cells as you want. However, you are not allowed to touch the code below the line "=============".
# You need to implement the three (four for grads) searching functions and the print result functions.
# For the searching functions, feel free to customize the return data types and parameter lists as long as the function name is as required.
# 

