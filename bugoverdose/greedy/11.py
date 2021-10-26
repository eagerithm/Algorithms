# Hackerland Radio Transmitters (https://www.hackerrank.com/challenges/hackerland-radio-transmitters/problem)
# 안테나 설치

N, K = map(int, input().split())
houses = sorted(list(map(int, input().split())))

counter = 0
left_end = 0
covered = [False]*N

for cur in range(N):
    if covered[cur]: continue
    if cur+1 <= N-1:
        if houses[cur+1] <= houses[left_end]+K: continue

    counter += 1 # center == cur

    for next_idx in range(cur+1, N):
        if houses[cur]+K < houses[next_idx]:
            left_end = next_idx
            break
        covered[next_idx] = True

print(counter)

#  =================================================================