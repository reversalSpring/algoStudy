class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        if not tickets:
            return []
        
        route = {}
        for i in tickets:
            start, end = i[0], i[1]
            if start in route:
                route[start].append(end)
            else:
                route[start] = [end]
                
        for z, k in route.items():
            k.sort(reverse=True)
            
        print(route)
        
        sol = []
        cur = 'JFK'
        while route:
            if cur in route:
                sol.append(cur)
                next = route[cur].pop()
                if not route[cur]:
                    del route[cur]
                cur = next
                
        sol.append(cur)
        
        return sol