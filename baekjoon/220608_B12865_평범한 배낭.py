def knapsack_dp(w, n):
    arr = [[0 for _ in range(w+1)] for _ in range(n+1)]
    
    for i in range(1, n+1):
        for j in range(1, w+1):
            if weight_arr[i-1] > j:
                arr[i][j] = arr[i-1][j]
            else:
                arr[i][j] = max(value_arr[i-1]+arr[i-1][j-weight_arr[i-1]], arr[i-1][j])
    
    return arr[n][w]

N, K = map(int, input().split())
value_arr, weight_arr = [0 for _ in range(N)], [0 for _ in range(N)]
    
for i in range(N):
    weight_arr[i], value_arr[i] = map(int, input().split())
                
print(knapsack_dp(K, N))