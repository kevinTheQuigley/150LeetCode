class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        def preqListGen(numCourses,prerequisites):
            preqList = [[] for _ in range(numCourses)]

            for course,prereq in prerequisites:
                preqList[prereq]=course
            
            return preqList
            
        preqList = preqListGen(numCourses,prerequisites)

        inVertices = [0]*numCourses

        def findInVertices(prerequisites,inVertices):
            for course,prerequisite in prerequisites:
                inVertices[course]+=1
            return inVertices
            

        inVertices = findInVertices(prerequisites,inVertices)
        
        courseStack = []
        returnStack = []

        for course in range(numCourses):
            if inVertices[course]==0:
                courseStack.append(course)
        
        while len(courseStack)>0:
            print(inVertices,preqList)
            currentCourse = courseStack.pop()
            returnStack.append(currentCourse)
            for nextCourse in preqList[course]:
                inVertices[nextCourse]-=1
                if inVertices[nextCourse]==0:
                    courseStack.append(nextCourse)
        
        return returnStack

        
        


        