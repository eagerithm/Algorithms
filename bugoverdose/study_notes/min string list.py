# min(list) : list의 요소들 중 최소 값 출력
# 모든 요소가 문자열이면 가나다 정렬 기준 가장 작은 값 반환(a쪽)

x = min('red', 'green', 'blue')
print(x) # blue

# ==============================================
# min(list(list1, list2, list3))
# list1, list2, list3 중 가장 '작은 값' 출력. 가나다 정렬.
y = [["ICN", "SFO", "ATL", "ICN", "ATL", "SFO"], 
     ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]] 

print(min(y))
# ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"] 