import heapq

def solution(scoville, K):
    answer = 0
    hq = []
    
    for cur_scoville in scoville:
        heapq.heappush(hq, cur_scoville)
        
    while True:
        first_scoville = heapq.heappop(hq)
        
        # 종결 조건 1 - 스코빌 지수를 K 이상으로 만들 수 없는 경우
        if len(hq) == 0 and first_scoville < K:
            answer = -1
            break
        
        # 종결 조건 2 - 스코빌 지수가 모두 K 이상인 경우
        if first_scoville > K:
            break
        
        second_scoville = heapq.heappop(hq)
        heapq.heappush(hq, first_scoville + second_scoville * 2)
        answer += 1
    
    return answer
