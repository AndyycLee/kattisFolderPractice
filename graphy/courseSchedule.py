class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
 
        # we need a indegree map, and a preReq->Course Map

        prereqToCourse = {i: [] for i in range(numCourses)}
        indegreeMap = {i: 0 for i in range(numCourses)}

        # first we need to do the right mapping
        for course, preReq in prerequisites:
            indegreeMap[course] += 1
            prereqToCourse[preReq].append(course)

        q = collections.deque()

        for i in indegreeMap:            
            if indegreeMap[i] == 0:
                q.append(i)
                #res.append(course) -approach 2

        # we can start a BFS, now only adding neighbours that have no prereqs
        res = []
        while q:
            # could do the processing here, but personally I think the processing afterwards is more beautiful like
            course = q.popleft()
            res.append(course)
            for neighbourCourse in prereqToCourse[course]:
                
                indegreeMap[neighbourCourse] -= 1

                if indegreeMap[neighbourCourse] == 0:
                    q.append(neighbourCourse)
                    #    res.append(course) -approach 2 means I dont do:
                    #             res.append(course) in line 26

        if len(res) == numCourses:
            return res
        else:
            return []

    

    # class Solution:
    # def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    #     # kanhs algorihitim

    #     # we need twothings, first a prereqs map, second, a indegree map
    #     # adjList should point course -> prereqs

    #     prereqToCourse = {i:[] for i in range(numCourses) }
    #     courseIndegree = {i:0 for i in range(numCourses) } # defaultdict(int) doesnt work cuz it doesnt init i: 0

    #     for course, prereq in prerequisites:
    #         prereqToCourse[prereq].append(course)
    #         courseIndegree[course] += 1

    #     res = []
    #     q = collections.deque()

    #     # first need to create the empty bfs

    #     for course in courseIndegree: # numCourses
    #         if courseIndegree[course] == 0: # could also do [] if prereqToCourse
    #             q.append(course)
    #             res.append(course)
    #     # now we need to do the bfs

    #     while q:
    #         course = q.popleft()
            
    #         # so now, add the neighbours
    #         for prereq in prereqToCourse[course]:
    #             courseIndegree[prereq] -= 1
    #             if courseIndegree[prereq] == 0:
    #                 q.append(prereq)
    #                 res.append(prereq)

    #     if len(res) == numCourses:
    #         return res
    #     else:
    #         return []