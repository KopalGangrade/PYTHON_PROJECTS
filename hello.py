# 3 6 2 1 7 2 5 6 1

# arr=list(map(int,input().split()))
# i=0
# store=[]
# while i < len(arr)-1:
#     sum=arr[i]+arr[i+1]
#     store.append(sum)
#     i+=1
# print(store)
# j=0
# max=store[0]
# while j<len(store):
#     if max<store[j]:
#         new_arr = store[j]
#     j+=1
# print(new_arr)



arr=list(map(int,input().split()))
i=0
m=arr[0]
while i < len(arr)-1:
    sum_=arr[i]+arr[i+1]
    if (m<sum_):
        m=sum_ 
    i+=1
print(m)



        

    # store.append(sum)
# print(store)
# j=0
# max=store[0]
# while j<len(store):
#     if max<store[j]:
#         new_arr = store[j]
#     j+=1
# print(new_arr)


# You are given an array of integers and another integer K. Print the first element of the array that is greater than K. If there are no elements greater than K, print No.

# Sample Input 1
# 3 5 10 25 16 12 14
# 11
# Sample Output 1
# 25
# Explanation: In the given array, the first element greater than 11 is 25.


# Sample Input
# 3 2 1
# Sample Output
# 3
# 3 2
# 3 2 1
# 2
# 2 1
# 1


# 1 2 3 4

# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4
# 2 
# 2 3 
# 2 3 4
# 3
# 3 4
# 4




    
