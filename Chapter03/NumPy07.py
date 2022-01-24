# 병합과 분리

# 병합 : concatenate
import numpy as np

list1 = [1,2,3]
list2 = [4,5,6]

print(list1)
print(list2)

print("\n")

list = np.concatenate([list1,list2])

print(list)

list = np.concatenate([list1,list2], axis=0)    # axis는 파라미터를 이용해 방향을 지정한다.
print(list)

list1 = [[1,2,3],[4,5,6]]
list2 = [[7,8,9],[10,11,12]]

list = np.concatenate([list1,list2], axis=0)    # axis = 0 으로 설정해 세로 방향으로 병합
print(list)
list = np.concatenate([list1,list2],axis=1)     # axis = 1 으로 설정해 가로 방향으로 병합
print(list)
print("---------------------------------")

# 3차원의 경우 axis가 0,1,2 가 존재함

vslist = np.vstack([list1,list2])               # axis = 0 과 동일 (수직 병합)
print(vslist)

hslist = np.hstack([list1,list2])               # axis = 1 과 동일 (수평 병합)
print(hslist)

print("---------------------------------")

# .stack() 함수는 차원(축)이 늘어나는 방법으로 병합
stlist = np.stack((list1,list2),0)  # 3차원 배열로 병합 # 0은 맨 앞 축  # 축 번호 생략시 0으로 처리
print(stlist)                       
print(stlist.shape)                 # (2,2,3)
print("\n")

stlist = np.stack((list1,list2),-1)  # 3차원 배열로 병합 # -1은 마지막 축 번호  
print(stlist)                       # 
print(stlist.shape)                 # (2,3,2)
print("\n")

stlist = np.stack((list1,list2),1)  # 3차원 배열로 병합 # 1번 축, 즉, 중간 축에 추가됨
print(stlist)
print(stlist.shape)                 # (2,2,3)
print("\n")

print(list1)
print(list2)