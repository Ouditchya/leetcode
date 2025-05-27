from collections import defaultdict

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        v, q = len(values), len(queries)
        map_ev, adj = {}, defaultdict(list)
        for i in range(v):
            map_ev[(equations[i][0], equations[i][1])] = values[i]
            map_ev[(equations[i][1], equations[i][0])] = 1/values[i]
            adj[equations[i][0]].append(equations[i][1])
            adj[equations[i][1]].append(equations[i][0])

        def find_path(node, visited, ls):
            nonlocal path, flag, target

            if flag: return

            if node == target: 
                ls.append(node)
                path = ls[:]
                flag = True
                return
            
            if visited.get(node, 0) == 1: return
            visited[node] = 1
            ls.append(node)

            for next_node in adj[node]: find_path(next_node, visited, ls)
            ls.pop()

        def solve_path(path):
            val, n = 1.0, len(path)
            for j in range(1, n): val *= map_ev[(path[j-1], path[j])]
            return val

        ans = []
        for i in range(q):
            if adj.get(queries[i][0], 0) == 0 or adj.get(queries[i][1], 0) == 0: ans.append(-1.0)
            elif map_ev.get((queries[i][0], queries[i][1]), 0) != 0: ans.append(map_ev[(queries[i][0], queries[i][1])])
            elif queries[i][0] == queries[i][1]: ans.append(1.0)
            else: 
                source, target = queries[i][0], queries[i][1]
                path, flag = [], False
                
                find_path(source, {}, [])
                if len(path) == 0: query_result = -1.0
                else: query_result = solve_path(path)
                ans.append(query_result)
                map_ev[(source, target)] = query_result
                map_ev[(target, source)] = 1/query_result

        return ans