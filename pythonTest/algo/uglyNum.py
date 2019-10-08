import heapq

class Solution:
    def nthUglyNumber(self, n):
        heap = [1]
        visited = set([1])
        
        val = None
        for i in range(n):
            val = heapq.heappop(heap)
            for multi in [2, 3, 5]:
                if val * multi not in visited:
                    visited.add(val * multi)
                    heapq.heappush(heap, val * multi)
	    print(heapq.heappop(heap))

        return val

solution = Solution()
val = solution.nthUglyNumber(100)
print(val)
