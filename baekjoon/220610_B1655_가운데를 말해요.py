import sys 
import heapq # 디폴트가 최소힙

N = int(sys.stdin.readline())

left_heap = [] # max heap
right_heap = [] # min heap
answer = []

for i in range(1, N+1):
    cur = int(sys.stdin.readline())
    
    if i % 2 == 1:
        # 홀수번째이면 
        # 오른쪽에 넣어서 오른쪽 최소수를 꺼내 왼쪽에 넣는다.
        heapq.heappush(right_heap, cur)
        heapq.heappush(left_heap, -heapq.heappop(right_heap))
        
    else:
        # 짝수번째이면
        # 왼쪽에 넣어서 왼쪽 최대수를 꺼내 오른쪽에 넣는다.
        heapq.heappush(left_heap, -cur)
        heapq.heappush(right_heap, -heapq.heappop(left_heap))
        
    answer.append(-left_heap[0])
    
for num in answer:
    print(num)




