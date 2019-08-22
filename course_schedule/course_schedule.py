from collections import defaultdict, deque
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        
        coursesGraph = defaultdict(list)
        coursePrerequisitesCount = defaultdict(int)
        s = set()
        for i in range(len(prerequisites)):
            course, prerequisite = prerequisites[i]
            coursesGraph[prerequisite].append(course)
            coursePrerequisitesCount[course] += 1
            s.add(prerequisite)
            s.add(course)
            
        for i in s:
            if i not in coursePrerequisitesCount:
                coursePrerequisitesCount[i] = 0
            
            
        print(coursePrerequisitesCount)
        print(coursesGraph)
        
        finishedCourses = deque()
        finishedCoursesCount = 0
    
        for course in coursePrerequisitesCount:
            if coursePrerequisitesCount[course] == 0:
                finishedCourses.append(course)
       
        while finishedCourses:
            currentCourse = finishedCourses.popleft()
            print("course: ", currentCourse)
            finishedCoursesCount += 1
            
            for nextCourse in coursesGraph[currentCourse]:
                coursePrerequisitesCount[nextCourse] -= 1
                if coursePrerequisitesCount[nextCourse] == 0:
                    finishedCourses.append(nextCourse)
        print(finishedCoursesCount)
        
        return True if (finishedCoursesCount == len(s)) else False
        