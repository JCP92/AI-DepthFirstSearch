
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

# In[ ]:


#implementation of function "aStarMisplacedTiles"
import time
import numpy as np
import sys
#from queue import PriorityQueue


goalState = [0, 1, 2, 3, 4, 5, 6, 7, 8]
mResults = []
mMoves = []
mIterations = []
mSteps = []
mTimer = []


goalState = [0, 1, 2, 3, 4, 5, 6, 7, 8]
def printBoard(curState):
    if curState == None:
        print("NONE")
    else:
        print("-------------")
        print("| %i | %i | %i |" % (curState[0], curState[1], curState[2]))
        print("-------------")
        print("| %i | %i | %i |" % (curState[3], curState[4], curState[5]))
        print("-------------")
        print("| %i | %i | %i |" % (curState[6], curState[7], curState[8]))
        print("-------------")

class Node(object):
    def __init__(self, state, parent, operator, depth, cost):
        self.state = state
        self.parent = parent
        self.operator = operator
        self.depth = depth
        self.cost = cost
        self.left = None
        self.up = None
        self.down = None
        self.right = None            
    
        
def mUp(curState):
    nState = list(curState)
    ID = nState.index(0)
    nState[ID], nState[(ID-3)] = nState[(ID-3)], nState[ID]
    mSteps.append(1)
    return nState
                
def mLeft(curState):
    nState = list(curState)
    ID = nState.index(0)
    nState[ID], nState[(ID-1)] = nState[(ID-1)], nState[ID]
    mSteps.append(1)
    return nState
    
def mRight(curState):
    #print(curState)
    nState = list(curState)
    ID = nState.index(0)
    nState[ID], nState[(ID+1)] = nState[(ID+1)], nState[ID]
    mSteps.append(1)
    return nState
    
def mDown(curState):
    nState = list(curState)
    ID = nState.index(0)
    nState[ID], nState[(ID+3)] = nState[(ID+3)], nState[ID]
    mSteps.append(1)
    return nState

def checkL(state):
    ID = state.index(0)
    if (ID != 0) & (ID != 3) & (ID != 6):
        return True
    else:
        return False

def checkU(state):
    ID = state.index(0)
    if (ID != 0) & (ID != 1) & (ID != 2):
        return True
    else:
        return False

def checkR(state):
    ID = state.index(0)
    #print(ID)
    if (ID != 2) & (ID != 5) & (ID != 8):
        return True
    else:
        return False

def checkD(state):
    ID = state.index(0)
    if (ID != 6) & (ID != 7) & (ID != 8):
        return True
    else:
        return False

def compState(state):
    for i in range (9):
        if state[i] != goalState[i]:
            return False
    print("true")
    return True

def heurstic(state):
    score = 0
    for i in range(9):
        if state[i] != goalState[i]:
            score += 1
    return score

def numMis( state ):
    count = 0
    for i in range(9):
        if (state[i] != i):
            count = count + 1
    return count
        
        
                

def aStar(root, i):
    myQueue = []
    mIterations.append(1)
    if compState(root.state) == True:
        print("true")
        mMoves.insert(0, root.operator)
        return mResults.insert(0, root.state)
    if (i == 8):
            mIterations.append(1)
            return
    if checkL(root.state) == True & (root.left == None):
        #print("L")
        root.left = Node(mLeft(root.state), root.state, "l", root.depth+1, 0)
        root.left.cost = numMis(root.left.state)
        print(root.left.cost)
        myQueue.append(root.left.cost)
        if(compState(mResults[0]) == True):
            mMoves.append(root.operator)
            return mResults.append(root.left.state)
    if checkU(root.state) == True & (root.up == None):
        print("U")
        root.up = Node(mUp(root.state), root.state, "u", root.depth+1, 0)
        root.up.cost = numMis(root.up.state)
        myQueue.append(root.up.cost)
        if(compState(mResults[0])):
            mMoves.append(root.operator)
            return mResults.append(root.up.state)
    if checkD(root.state) == True & (root.down == None):
        #print("D")
        root.down = Node(mDown(root.state), root.state, "d", root.depth+1, 0)
        root.down.cost = numMis(root.down.state)
        myQueue.append(root.down.cost)
        if(compState(results[0])):
            mMoves.append(root.operator)
            return mResults.append(root.down.state)
    if checkR(root.state) == True & (root.right == None):
        root.right = Node(mRight(root.state), root.state, "r", root.depth+1, 0)
        root.right.cost = numMis(root.right.state)
        myQueue.append(root.right.cost)
        if(compState(mResults[0])):
            mMoves.append(root.operator)
            return mResults.append(root.right.state)
    l = r = u = d = 0
    
    while myQueue != []:
        m = myQueue.pop()
        if root.left != None: 
            if(m == root.left.cost) & (l==1): aStar(root.left, i+1)
        if root.right != None: 
            if(m == root.right.cost) & (r==1): aStar(root.right, i+1)
        if root.up != None: 
            if(m == root.up.cost) & (u==1): aStar(root.up, i+1)
        if root.down != None: 
            if(m == root.down.cost) & (l==1): aStar(root.down, i+1)
              
    return

        

def main():
    f = open("8puz.txt", "r")
          
    for n in range(1): 
        line = f.readline().split(', ')
        line =[int(i) for i in line]
        inState = line
        inState = [3, 1, 2, 0, 4, 5, 6, 7, 8]
        root = Node(inState, None, "Start", 0, None)
        mResults.append(root.state)
        aStar(root, 0)
    
    mMoves.reverse()
    mResults.reverse()
    if results[0] == None:
        print("None")
    else:
        for i in range(len(mResults)):
            printBoard(results[i])
    print("Average Steps\t" + str(np.sum(steps)))
    f.close()

main()


# In[ ]:


#implementation of function "aStarManhattanDistance"
#implementation of function "aStarMisplacedTiles"
#implementation of function "Iterative_deepening_DFS"
import time
import numpy as np
import sys
#from queue import PriorityQueue


goalState = [0, 1, 2, 3, 4, 5, 6, 7, 8]
aResults = []
aMoves = []
aIterations = []
aSteps = []
aTimer = []


goalState = [0, 1, 2, 3, 4, 5, 6, 7, 8]
def printBoard(curState):
    if curState == None:
        print("NONE")
    else:
        print("-------------")
        print("| %i | %i | %i |" % (curState[0], curState[1], curState[2]))
        print("-------------")
        print("| %i | %i | %i |" % (curState[3], curState[4], curState[5]))
        print("-------------")
        print("| %i | %i | %i |" % (curState[6], curState[7], curState[8]))
        print("-------------")

class Node(object):
    def __init__(self, state, parent, operator, depth, cost):
        self.state = state
        self.parent = parent
        self.operator = operator
        self.depth = depth
        self.cost = cost
        self.left = None
        self.up = None
        self.down = None
        self.right = None        
        
        
def mUp(curState):
    print(curState)
    nState = list(curState)
    ID = nState.index(0)
    nState[ID], nState[(ID-3)] = nState[(ID-3)], nState[ID]
    aSteps.append(1)
    return nState
                
def mLeft(curState):
    print(curState)
    nState = list(curState)
    ID = nState.index(0)
    nState[ID], nState[(ID-1)] = nState[(ID-1)], nState[ID]
    aSteps.append(1)
    return nState
    
def mRight(curState):
    print(curState)
    nState = list(curState)
    ID = nState.index(0)
    nState[ID], nState[(ID+1)] = nState[(ID+1)], nState[ID]
    aSteps.append(1)
    return nState
    
def mDown(curState):
    print(curState)
    nState = list(curState)
    ID = nState.index(0)
    nState[ID], nState[(ID+3)] = nState[(ID+3)], nState[ID]
    aSteps.append(1)
    return nState

def checkL(state):
    ID = state.index(0)
    if (ID != 0) & (ID != 3) & (ID != 6):
        return True
    else:
        return False

def checkU(state):
    ID = state.index(0)
    if (ID != 0) & (ID != 1) & (ID != 2):
        return True
    else:
        return False

def checkR(state):
    ID = state.index(0)
    #print(ID)
    if (ID != 2) & (ID != 5) & (ID != 8):
        return True
    else:
        return False

def checkD(state):
    ID = state.index(0)
    if (ID != 6) & (ID != 7) & (ID != 8):
        return True
    else:
        return False

def compState(state):
    for i in range (9):
        if state[i] != goalState[i]:
            return False
    print("true")
    return True

def heurstic(state):
    score = 0
    for i in range(9):
        if state[i] != goalState[i]:
            score += 1
    return score

def md2 ( state, col, row, i):
    m = np.reshape(state, (3,3))
    col2 = 0 
    row2 = 0
    for l in range (3):
        for n in range (3):
            if(m[l][n] == i):
                col2 = n
                row2 = l
    num = abs(row2 - row)
    return(num + abs(col2 - col))
                
def md1(state):
    total = 0
    row = col = y = 0
    for i in range (9):
        total =+ md2(state, col, row, i)
        if (col == 3):
            col = 0
            row =+ 1
        if (row == 3):
            return total
    return total
        
        
                

def aStar(root, i):
    myQueue = []
    aIterations.append(1)
    if compState(root.state) == True:
        print("true")
        aMoves.insert(0, root.operator)
        return results.insert(0, root.state)
    if (i == 8):
            aIterations.append(1)
            return
    if checkL(root.state) == True & (root.left == None):
        #print("L")
        root.left = Node(mLeft(root.state), root.state, "l", root.depth+1, 0)
        root.left.cost = md1(root.left.state)
        print(root.left.cost)
        myQueue.append(root.left.cost)
        if(compState(results[0]) == True):
            aMoves.append(root.operator)
            return aResults.append(root.left.state)
    if checkU(root.state) == True & (root.up == None):
        print("U")
        root.up = Node(mUp(root.state), root.state, "u", root.depth+1, 0)
        root.up.cost = md1(root.up.state)
        myQueue.append(root.up.cost)
        if(compState(results[0])):
            aMoves.append(root.operator)
            return aResults.append(root.up.state)
    if checkD(root.state) == True & (root.down == None):
        #print("D")
        root.down = Node(mDown(root.state), root.state, "d", root.depth+1, 0)
        root.down.cost = md1(root.down.state)
        myQueue.append(root.down.cost)
        if(compState(results[0])):
            aMoves.append(root.operator)
            return aResults.append(root.down.state)
    if checkR(root.state) == True & (root.right == None):
        root.right = Node(mRight(root.state), root.state, "r", root.depth+1, 0)
        root.right.cost = md1(root.right.state)
        myQueue.append(root.right.cost)
        if(compState(results[0])):
            aMoves.append(root.operator)
            return aResults.append(root.right.state)
    l = r = u = d = 0
    
    while myQueue != []:
        m = myQueue.pop()
        if root.left != None: 
            if(m == root.left.cost) & (l==1): aStar(root.left, i+1)
        if root.right != None: 
            if(m == root.right.cost) & (r==1): aStar(root.right, i+1)
        if root.up != None: 
            if(m == root.up.cost) & (u==1): aStar(root.up, i+1)
        if root.down != None: 
            if(m == root.down.cost) & (l==1): aStar(root.down, i+1)
              
    return

        

def main():
    f = open("8puz.txt", "r")
          
    for n in range(5): 
        line = f.readline().split(', ')
        line =[int(i) for i in line]
        inState = line
        root = Node(inState, None, "Start", 0, None)
        aStar(root, 0)
    
    aMoves.reverse()
    mResults.reverse()
    if mResults[0] == None:
        print("None")
    else:
        for i in range(len(mResults)):
            printBoard(mResults[i])
    print("Average Steps\t" + str(np.sum(steps)))
    f.close()

main()


# In[ ]:


#implementation of function "breadthFirstSearch" (for graduate students)


# In[ ]:


#implementation of function "print_result(result)"
result = 7
def print_result( result ):
    file = open("result.txt", "w")

    file.write("IDS\t"+ "\n")
    file.write("\tAverage Steps\t" + str((np.sum(steps))) + "\n")
    file.write("\tAverage Iterations\t" + str((np.sum(iterations)) + "\n"))
    file.write("\tAverage Iterations\t" + str((np.sum(timer))) + "\n")
    
    file.write("Manhanton\t"+ "\n")
    file.write("\tAverage Steps\t" + str((np.sum(aSteps)/5)) + "\n")
    file.write("\tAverage Iterations\t" + str((np.sum(aIterations)) + "\n"))
    file.write("\tAverage Iterations\t" + str((np.sum(aTimer)) + "\n"))
    
    file.write("Manhanton\t"+ "\n")
    file.write("\tAverage Steps\t" + str((np.sum(mSteps)) + "\n"))
    file.write("\tAverage Iterations\t" + str((np.sum(mIterations))) + "\n")
    file.write("\tAverage Iterations\t" + str((np.sum(mTimer))) + "\n")
    
    file.close()
    print("file closed")  


# In[ ]:


#implementation of function "Iterative_deepening_DFS"
goalState = [0, 1, 2, 3, 4, 5, 6, 7, 8]

import numpy as np
import sys

def printBoard(curState):
    print("-------------")
    print("| %i | %i | %i |" % (curState[0], curState[1], curState[2]))
    print("-------------")
    print("| %i | %i | %i |" % (curState[3], curState[4], curState[5]))
    print("-------------")
    print("| %i | %i | %i |" % (curState[6], curState[7], curState[8]))
    print("-------------")

def mUp(curState):
    nState = curState
    ID = nState.index(0)
    if (ID != 0) & (ID != 1) & (ID != 2):
        nState[ID], nState[(ID-3)] = nState[(ID-3)], nState[ID]
        #print("up")
        #printBoard(nState)
        return nState
    else:
        return None
                
    
def mLeft(curState):
    nState = curState
    ID = nState.index(0)
    if (ID != 0) & (ID != 3) & (ID != 6):
        nState[ID], nState[(ID-1)] = nState[(ID-1)], nState[ID]
        #print("l")
        #printBoard(nState)
        return nState
    else:
        return None
    
def mRight(curState):
    nState = curState
    ID = nState.index(0)
    if (ID != 2) & (ID != 5) & (ID != 8):
        nState[ID], nState[(ID+1)] = nState[(ID+1)], nState[ID]
        #print("r")
        #printBoard(nState)
        return nState
    else:
        return None
    
def mDown(curState):
    nState = curState
    ID = nState.index(0)
    if (ID != 6) & (ID != 7) & (ID != 8):
        nState[ID], nState[(ID+3)] = nState[(ID+3)], nState[ID]
        #print("d")
        #printBoard(nState)
        return nState
    else:
        return None
    
def createNode (curState, parent, operator, level):
    return Node(curState, parent, operator, level)


def expandNodes (node, nodes):
    exNodes = []
    exNodes.append( createNode(mLeft(node.state), node, "l", node.depth+1))
    exNodes.append( createNode(mUp(node.state), node, "u", node.depth+1))
    exNodes.append( createNode(mDown(node.state), node, "d", node.depth+1))
    exNodes.append( createNode(mRight(node.state), node, "r", node.depth+1))
    exNodes = [node for node in exNodes if node.state != None]
    return exNodes

def DFS( start, goalState, depth = 10):
    dLimit = depth
    nodes = []
    nodes.append(createNode(start, None, None, 0))

    while True:
        if len(nodes) == 0:
            return None
        node = nodes.pop(0) #front of queue
        
        if node.state == goalState:
            print("In")
            moves = []
            temp = node
            while True:
                moves.insert(0, temp.operator)
                print("1")
                if temp.level <= 1:
                    break
                temp = temp.parent
            return moves

        if node.depth < dLimit:
            exNodes = expandNodes(node, nodes)
            exNodes.extend(nodes)
            print(exNodes[2].state)
            nodes = exNodes

def IDS (start, goalState, level = 40):
    for i in range ( level ):
        result = DFS(start, goalState, i)
        print(i)
        if result != None:
            return result

class Node:
    def __init__ ( self, state, parent, operator, depth):
        self.state = state
        self.parent = parent
        self.operator = operator
        self.depth = depth

    

def main():
    f = open("8puz.txt", "r")
          
    for n in range(100): 
        line = f.readline().split(', ')
        line =[int(i) for i in line]
    
    inState = [1, 0, 2, 3, 4, 5, 6, 7, 8]
    printBoard(inState)
    result = IDS(inState, goalState)
    if result == None:
        print("None")
    elif result == [None]:
        print("start node was goal")
    else:
        print (result)
        print (len(result), "moves")

main()


# You can insert as many cells as you want above
# You are not Allowed to modify the code below this line.
# ===============================

# In[ ]:


#you need to implement print_result function to print out the result according to the required format
print_result(result)


# 
# The output format should be as follows. You only need to give one sample solution as an example.
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Solution of the first Scenario:
# X X X
# X X X
# X X X
# to
# X X X
# X X X
# X X X
# to
# X X X
# X X X
# X X X
# to
# X X X
# X X X
# X X X
# to
# .
# .
# .
# 0 1 2
# 3 4 5
# 6 7 8
# 
#                 Average_Steps    Average_Time   Average_Iterations   
# UCS
# A*(Misplaced)
# A*(Manhattan)
# BFS
# 
# 

# In[ ]:


#implementation of function "Iterative_deepening_DFS"
import time
import numpy as np
import sys

goalState = [0, 1, 2, 3, 4, 5, 6, 7, 8]
results = []
iterations = []
moves = []
steps = []
timer = []
dLimit = 10




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
        
    def printPath(self):
        state = [self.state]
        operations = [self.operation]
        depth = [self.depth]

        
    def printPath(self):
        statePath = [self.state]
        operatorPath = [self.operator]
        depthPath = [self.depth]
        i = 0
        while self.parent:
            self = self.parent
            statePath.append(self.state)
            operatorPath.append(self.operator)
            depthpath.append(self.depth)
        while statePath:
            print('Move: ' + str(i) + ' Action: ' + str(operatorPath.pop()) + ' Depth: ' + str(depthPath.pop()))
            print(statePath.pop())
            i += 1
        
        

    def DFS(self):
        start = time.time()

        que = [self]
        quePopper = 0
        queMaxCounter = 1

        queNodeDepth = [0]
        pathCost = [0]
        visited = []
        
        while que is not None:
            if len(que) > queMaxCounter:
                queMaxCounter = len(que)
            curNode = que.pop(0)
            quePopper =+ 1

            curDepth = queNodeDepth.pop(0)
            curPathCost = pathCost.pop(0)
            visited.append(curNode.state.copy())
            
            print('Starting: ')
            print(curNode.state)
            if curNode.compState(curNode.state):
                curNode.printBoard() #check coding
                print('Time Performance: ', str(quePopper), ' nodes popped off the queue')
                print('Space Performance: ', str(queMaxCounter), ' noeds in the queue at its max')
                print('time spent: %0.2fs' % (time.time() - start))
                return true
            else:
                if (curNode.swapCheck(curNode.state, -1)):
                    curNode.left = Node(curNode.doSwap(curNode.state, -1), curNode.state, 'l', curNode.depth + 1)
                    if (curNode.left.state not in visited):
                        que.insert(0, curNode.left)
                        queNodeDepth.insert(0, curNode.left.depth)
                        pathCost.insert(0, (curNode.state[curNode.state.index(0) - 1] + curPathCost))
                        print("L: " + str(curNode.left.state))

                if (curNode.swapCheck(curNode.state, 1)):
                    curNode.right = Node(curNode.doSwap(curNode.state, 1), curNode.state, 'r', curNode.depth + 1)
                    if (curNode.right.state not in visited):
                        que.insert(0, curNode.right)
                        queNodeDepth.insert(0, curNode.right.depth)
                        pathCost.insert(0, (curNode.state[curNode.state.index(0) + 1] + curPathCost))
                        print("R: " + str(curNode.right.state))

                if (curNode.swapCheck(curNode.state, -3)) :
                    curNode.up = Node(curNode.doSwap(curNode.state, -3), curNode.state, 'u', curNode.depth + 1)
                    if (curNode.up.state not in visited):
                        que.insert(0, curNode.up)
                        queNodeDepth.insert(0, curNode.up.depth)
                        pathCost.insert(0, (curNode.state[curNode.state.index(0) - 3] + curPathCost))
                        print("U: " + str(curNode.up.state))

                if (curNode.swapCheck(curNode.state, +3)):
                    curNode.down = Node(curNode.doSwap(curNode.state, +3), curNode.state, 'd', curNode.depth + 1)
                    if (curNode.down.state not in visited):
                        que.insert(0, curNode.down)
                        queNodeDepth.insert(0, curNode.down.depth)
                        pathCost.insert(0, (curNode.state[curNode.state.index(0) + 3] + curPathCost))
                        print("D: " + str(curNode.down.state))
           
    def swapCheck(self, curState, val):
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
    def doSwap(self, nState, val):
        copy = nState.copy()
        index = nState.index(0)
        copy[index], copy[index + val] = copy[(index + val)], copy[index]
        return copy
    def compState(self, state):
        for i in range (9):
            if state[i] != goalState[i]:
                return False
        return True




        
        
        
    
        
        

def IDS (inState):
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
        
    print(results[0])
    print(steps)

    moves.reverse()
    results.reverse()
    print(results[0])
    if results[0] == None:
        print("None")
    else:
        for i in range(len(results)):
            printBoard(results[i])
    print("Average Steps\t" + str(np.sum(steps)))
    f.close()

main()

