class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n=len(isConnected)
        graph=collections.defaultdict(list)
        for i in range(n):
            for j in range(i+1,n):
                if isConnected[i][j]:
                    graph[i].append(j)
                    graph[j].append(i)
        def dfs(src):
            for next_node in graph[src]:
                if next_node not in seen:
                    seen.add(next_node)
                    dfs(next_node)
        seen=set()
        ans=0
        for i in range(n):
            if i not in seen:
                ans+=1
                seen.add(i)
                dfs(i)
        return ans