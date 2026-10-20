list1=["abhinav","aman","abhinav","yash","aman","rahul","abhinav","yash"]
freq={}
for name in list1:
    if name not in freq:
        freq[name]=1
    else:
        freq[name]+=1
print(freq)
