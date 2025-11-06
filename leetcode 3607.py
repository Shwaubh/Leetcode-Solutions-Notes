class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        data = defaultdict(list)
        heaps = defaultdict(list)
        for u, v in connections:
            data[u].append(v)
            data[v].append(u)
        
        leaders = defaultdict(int)
        visited = set()
        for node in range(1, c+1):
            q = deque()
            if node in visited:
                continue
            visited.add(node)
            leaders[node] = node
            for n in data[node]:
                q.append(n)
            
            while q:
                temp = q.popleft()
                leaders[temp] = node
                visited.add(temp)
                for n in data[temp]:
                    if n not in visited:
                        q.append(n)
        for u, v in connections:
            heapq.heappush(heaps[leaders[u]], u)
            heapq.heappush(heaps[leaders[v]], v)

        res = []
        for op, node in queries:
            if op == 2:
                visited.discard(node)
            else:
                if node in visited:
                    res.append(node)
                    continue
                while heaps[leaders[node]]:
                    top = heaps[leaders[node]][0]
                    if top in visited:
                        res.append(top)
                        break
                    else:
                        heapq.heappop(heaps[leaders[node]])
                else:
                    res.append(-1)

        return res
                
            

