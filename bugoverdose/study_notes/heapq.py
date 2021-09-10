# min heap에서 최대값만 제거하기
import heapq 

heap = [2, 4, 1, 7, 3, 8, 5, 4, 4, 4]
heapq.heapify(heap)

# nlargest를 통해 최대~최소로 전부 조회, index=0을 제외하고 전부 min heap으로 다시 정렬
heap = heapq.nlargest(len(heap), heap)[1:]
heapq.heapify(heap)

# ==============================================================
# max heap 만들기
from heapq import *

nums = [2, 4, 1, 7, 3, 8, 5, 4, 4, 4]
heap = []
for num in nums:
    heappush(heap, (-num, num)) # -num을 기준으로 minheap을 만들고 num을 사용하면 maxheap

print([v for i, v in heap]) # [8, 4, 7, 4, 4, 1, 5, 2, 4, 3]

# ==============================================================
import heapq as hq
 
# the dictionary to be as heap
my_dict = {'z': 'zebra', 'b': 'ball', 'w': 'whale',
           'a': 'apple', 'm': 'monkey', 'c': 'cat'}
 
# conversion to tuple
my_list = [(k, v) for k, v in my_dict.items()]
 
print("Before organizing as heap :", my_list)
# Before organizing as heap : [(‘z’, ‘zebra’), (‘b’, ‘ball’), (‘w’, ‘whale’), (‘a’, ‘apple’), (‘m’, ‘monkey’), (‘c’, ‘cat’)] 
 
hq.heapify(my_list) # arrange as min-heap
 
print("After organizing as heap :", my_list)
# After organizing as heap : [(‘a’, ‘apple’), (‘b’, ‘ball’), (‘c’, ‘cat’), (‘z’, ‘zebra’), (‘m’, ‘monkey’), (‘w’, ‘whale’)] 
 
# re convert to dictionary
my_dict = dict(my_list)
 
print("Resultant dictionary :", my_dict)
# Resultant dictionary : {‘a’: ‘apple’, ‘b’: ‘ball’, ‘c’: ‘cat’, ‘z’: ‘zebra’, ‘m’: ‘monkey’, ‘w’: ‘whale’}

# ==============================================================