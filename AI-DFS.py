#implementation of function "DFS"
import time
import numpy as np
import sys
goalState = [0, 1, 2, 3, 4, 5, 6, 7, 8]
que = []
quePopper = 0
queMaxCounter = 0
queNodeDepth = [1]
pathCost = [0]
visited = []



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
        global que, quePopper, queMaxCounter, queNodeDepth, pathCost, visited
        que.insert(0, self) #initialization of que


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
            if np.array_equal(curNode.state, goalState):
                curNode.printPathway()
                print('Time: ', str(quePopper), ' nodes popped off the queue')
                print('Space: ', str(queMaxCounter), ' nodes in the queue at its max')
                print('time spent: %0.2fs' % (time.time() - start))
                return true
            else:
                curNode.left = curNode.expandNode(-1, 'l', curPathCost)
                curNode.right = curNode.expandNode(1, 'r', curPathCost)
                curNode.up = curNode.expandNode(-3, 'u', curPathCost)
                curNode.down = curNode.expandNode(3, 'd', curPathCost)

def expandNode(self, val, direction, curPathCost):
    if (self.swapCheck(val)): #expand node
        pntr = Node(self.doSwap(val), self.state, direction, self.depth + 1)#store expanded node
        if (pntr.state not in visited): #add to ques if not visited
            que.insert(0, pntr)
            queNodeDepth.insert(0, pntr.depth)
            pathCost.insert(0, (self.state[self.state.index(0) + val] + curPathCost))
            print(direction + ": " + str(pntr.state))
            return pntr;
        else:
            return None

def swapCheck(self, val): #verify if able to swap
    index = self.state.index(0)
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

def doSwap(self, val): #swap it
    copy = self.state.copy()
    index = self.state.index(0)
    copy[index], copy[index + val] = copy[(index + val)], copy[index]
    return copy

def printBoard(self, state):
    if curState == None:
        print("NONE")
    else:
        print("-------------")
        print("| %i | %i | %i |" % (state[0], state[1], state[2]))
        print("-------------")
        print("| %i | %i | %i |" % (state[3], state[4], state[5]))
        print("-------------")
        print("| %i | %i | %i |" % (state[6], state[7], state[8]))
        print("-------------")

def printPathway(self):
    statePath = self.state
    directionPath = self.operator
    depthPath = self.depth
    i = 0
    while (self.parent):
        self = self.parent
        statePath.append(self.state)
        directionPath.append(self.operator)
        depthPath.append(self.depth)
    while statePath:
        print("Step: " + i + "\tDirection: " + directionPath.pop() +"\tDepth: " + depthPath.pop())
        self.printBoard(statePath.pop())


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
