"""
Course Schedule
"""

## Method 3 Using Kahns Algorithm
##  arrange all the vertices so that one leads to another
## Cycle through all, if there was one extra in the count, then they are removed

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def genPreqList(numCourses,prerequisites):
            preqList = [[] for _ in range(numCourses)]

            for (course,prereq) in prerequisites:
                preqList[prereq].append(course)

            return preqList

        preqList = genPreqList(numCourses,prerequisites)

        def findInVertices(numCourses,prerequisites):
            inVertices =  [0]*numCourses
            for course,preq in prerequisites:
                inVertices[course]+=1

        inVertices=findInVertices(numCourses,prerequisites)

        stack = []
        for course in range(numCourses):
            if inVertices(course)==0:
                stack.append(course)
        counter = 0 
        def vertexCycle(vertex):
            counter+=1
            
            for nextCourse in preqList[vertex]:
                inVertices[nextCourse]-=1
                stack.append(nextCourse)
            
        while len(stack)>0:
            course = stack.pop()
            vertexCycle(course)

        if counter>numCourses:
            return False
        else:
            return True
            
        




"""
Course Schedule
"""

## Method 1 Using a visited list with a DFS function
## On first pass while iterating, course is set to -1
## At the end of the function, it's set to 1

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def genPreqList(numCourses,prerequisites):
            preqList = [[] for _ in range(numCourses)]

            for (course,prereq) in prerequisites:
                preqList[prereq].append(course)

            return preqList

        preqList = genPreqList(numCourses,prerequisites)

        courseStatus = numCourses*[0]

        def hasCycle(course):
            if courseStatus[course]==-1:
                return True
            elif courseStatus[course]==1:
                return False
            
            courseStatus[course]=-1

            for nextCourse in preqList[course]:
                if hasCycle(nextCourse):
                    return True
                
            courseStatus[course]=1
            return False

        for course in range(numCourses):
            if hasCycle(course):
                return False
        
        return True

        








            

        
        





























"""

possible
numCourses=2
prerequisites=[[1,0]]

impossible
numCourses=2
prerequisites=[[1,0],[1,0]]

Using  BFS
First generate a pre-req list
[[],[0],[1,0]]

Generate a visited set



Using DFS
First generate a pre-req dictionary
ie
{0:[1],1:[2]} -> We can use an empty series of lists
[[],[0],[1,0]]


Iterate over every value
Define a function to iteratively check for a cycle for each value
use a set of visited values at each cycle
-> A little slow with some nested for loops

Using Kahns Algo

"""







class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def generatePreqList(numCourses,prerequisites)->list:
            l = []
            for _ in numCourses:
                l.append([])
            
            for (i,j) in prerequisites:
                l[j].append(i)
            
            return l
        
        visitedSet = set()
        
        def checkForCycle(course):
            if course in visitedSet:
                return False
            else:
                visitedSet.append(course)
                return True

        preqList = generatePreqList(numCourses,prerequisites)


        for course in range(numCourses):
            visitedSet=set().add(course)
            currentCourses=[course]
            while currentCourses:
                if checkForCycle(course):
                    pass




# say adjList = [[1],[]]
# that 1 is a pre requisite for 0
prerequisites=[0,1]

#Showing the state, initialized to 
[0,0]
#on 0, first value is set to -1
[-1,0]
#1 is a prereq, is set to -1 too
[-1,-1]
#1 gets updated to 1
[-1,1]
#0 is set to 1
[1,1]



[[1,0],[0,1]]

#on 0
[-1,0]
[-1,1]


#on 1
[-1,-1]


"""



"""

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def genReqList(prerequisites):
            reqList=[ [] for _ in range(numCourses)]
            for (course,prereq)  in prerequisites:
                reqList[prereq].append(course)
            return reqList
            
        
        state = [0]*numCourses
        reqList = genReqList(prerequisites)

        def hasCycle(course)->bool:
            if state[course]==1:
                return False
            if state[course]==-1:
                return True
            
            state[course]=-1
            for pres in reqList[course]:
                if hasCycle(pres):
                    return True
            state[course]=1
            return False
        
        for course in range(numCourses):
            if hasCycle(course):
                return False
        
        return True













































"""
METHOD 1:-
Using DFS
First create a prerequisite dictionary of all course that are pre-requisites for other courses
ie
[1,0],[2,0]

Becomes
{0:[1,2]}

Take each element from the list of possible elements and iterate over them, ie [0,1,2]

Have a function that will check for a cycle during an iteration over each element. 
Function should be recursive, looking over each other element



"""

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:


















# Using Kahns algo:-
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:


        def convertToPreReqList(prerequisites,numCourses):
            preReqList=[[] for _ in range(numCourses)]
            for (course,pre) in prerequisites:
                preReqList[pre].append(course)
            
            return preReqList
        
        def detectCycle(preReqList,course,visitedSet):
            for nextCourse in preReqList[course]:
                if nextCourse in visitedSet:
                    return False
                else:
                    visitedSet.append(nextCourse)
                    return detectCycle(preReqList,nextCourse,visitedSet)


               
        

















##------> Using BFS
from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseDict= defaultdict(list)
        visited=set()

        def checkForCycle(course):
            values = courseDict[course]
            for value in values:
                if value in visited:
                    return False
            return True

        for course, pre in prerequisites:
            courseDict[pre].append(course)

        courseList= range(numCourses)
        for course in courseList:
            visited.add(course)
            if not checkForCycle(course):
                return False
        return True
            
