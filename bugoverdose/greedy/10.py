# Candies (https://www.hackerrank.com/challenges/candies/problem)
# Alice wants to give at least 1 candy to each child. If two children sit next to each other, 
# then the one with the higher rating must get more candies. 
# Alice wants to minimize the total number of candies she must buy.

N = int(input())

ratings = []
candy = [1]*N

for idx in range(N):
    ratings.append(int(input()))

min_num = min(ratings)
middles = []
for idx in range(N):
    if ratings[idx] == min_num:
        middles.append(idx)

M = len(middles)

for cur in range(M):
    min_num_idx = middles[cur]
    left_end = -1 if cur==0 else middles[cur-1]
    right_end = N if cur==M-1 else middles[cur+1]

    for idx in range(min_num_idx+1, right_end):
        if ratings[idx-1] < ratings[idx]:
            candy[idx] = max(candy[idx-1]+1, candy[idx])

    for idx in range(min_num_idx-1, left_end, -1):
        if ratings[idx] > ratings[idx+1]:
            candy[idx] = max(candy[idx+1]+1, candy[idx])

if middles[0] != 0:
    for idx in range(1, middles[0]):
        if ratings[idx-1] < ratings[idx]:
            candy[idx] = max(candy[idx-1]+1, candy[idx])

if middles[-1] != N-1:
    for idx in range(N-2, middles[M-1], -1):
        if ratings[idx] > ratings[idx+1]:
            candy[idx] = max(candy[idx+1]+1, candy[idx])

print(sum(candy))

#  =================================================================