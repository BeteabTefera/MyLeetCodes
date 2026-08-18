# Last updated: 8/18/2026, 2:50:09 PM
'''
U = number of coursed (0, N -1); prerequisites[i] = [ai, bi] shows that bi is the prerequisites needed for ai; example
   [0,1] to take course 0 i have to take course 1
   results needed: true if all courses can be finished otherwise false
   
M = I guess this is how topology sort is supposed to work, I am a little bit confused how the the verticies are being turned to a graph
P = in order to do topological sorting algorithm, we first need to be careful of cyclic edge cases
    example: [[0,1],[1,0]]
I
R
E


'''

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        graph=defaultdict(list)
        for course,prereq in prerequisites:
            graph[prereq].append(course)


        indegrees=[0]*numCourses
        for prereq,_ in prerequisites:
            indegrees[prereq]+=1


        queue=deque()
        for courses in range(numCourses):
            if indegrees[courses]==0:
                queue.append(courses)

        while queue:
            courses=queue.popleft()
            for prereq in graph[courses]:
                indegrees[prereq]-=1
                if indegrees[prereq]==0:
                    queue.append(prereq)


        return all(indegree==0 for indegree in indegrees)       