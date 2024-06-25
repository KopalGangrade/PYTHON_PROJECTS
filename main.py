# A=list(map(int,input().split()))
# i=0
# count=0
# B=[]
# while i < len(A)-1:
#     if (A[i]<=A[i+1]):
#         count+=1
#     i+=1
#     print(count)

A=list(map(int,input().split()))
i=0
count=0
B=[]
while i < (len(A)-1):
  if (A[i]<=A[i+1]):
    B.append(A[i])
    count+=1
  i+=1
print(B)

