class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans, n = [], len(graph)
        visited = [0] * n

        def traverse(ls, i):
            # Make 1st choice
            visited[i] = 1
            ls.append(i)
            # If destination reached, add path to ans
            if i == n-1: ans.append(ls[:])
            # Else make other choices
            else:
                for j in graph[i]:
                    if visited[j] != 1:
                        traverse(ls, j)
            # Backtrack 1st choice
            visited[i] = 0
            ls.pop()

        for i in graph[0]: traverse([0], i)

        return ans