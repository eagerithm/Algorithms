N, *arr = map(int, input().split()) # 4 10 20 30 40
# N == 4
# arr == [10, 20, 30, 40]

# ==============================================
print("".join(map(str, arr))) 
# 10203040

print(*arr) 
# 10 20 30 40

for num in arr:
    print(num)
# 10
# 20
# 30
# 40