num=[2,7,11,15]
target=int(input("Enter the target sum: "))
n=len(num)
dict1={}
for i in range(n):
    rem=target-num[i]
    if rem in dict1:
        print([dict1[rem],i])
    dict1[num[i]]=i
