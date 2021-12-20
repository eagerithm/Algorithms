A = 10
B = 12
arr_B = [int(i) for i in str(B)]  

print(arr_B) # [1, 2]

arr_B.reverse() # 원본을 변형. 반환값X

print(arr_B) # [2, 1]

print(arr_B[::-1]) # [1, 2] # 원본 불변. reverse한 배열을 반환

print(arr_B) # [2, 1]

for i in range(len(arr_B)):  
    print(A * arr_B[i])  
    # 20
    # 10